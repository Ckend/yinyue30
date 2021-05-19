# 使用官方 Python 轻量级镜像
# https://hub.docker.com/_/python
FROM python:3.8-slim
# 将本地代码拷贝到容器内
ENV APP_HOME /code
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
COPY . ./
# 安装依赖
RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential gcc \
                                        libsndfile1

RUN pip install Django pychorus librosa==0.6.0 numba==0.48.0

CMD exec python3 manage.py runserver 0.0.0.0:8000