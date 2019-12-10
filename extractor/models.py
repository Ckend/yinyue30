from django.db import models


class Document(models.Model):
    """
    文件模型
    @param models.Model: 继承模型对象
    """

    # upload_to 指定文件保存目录
    file = models.FileField(upload_to='media/%Y-%m-%d')
