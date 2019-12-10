from django.shortcuts import render
from django.http import HttpResponse
from .models import Document
from .forms import DocumentForm


def index(request):
    """
    单应用首页—文件上传
    @param request: 请求对象
    """
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(file=request.FILES['docfile'])
            newdoc.save()
            # 返回上传成功的消息
            return HttpResponse("上传成功！")
    else:
        # 生成一个空表
        form = DocumentForm()

    # 渲染表单
    return render(request, 'index.html', {'form': form})
