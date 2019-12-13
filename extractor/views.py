import os
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .models import Document
from .forms import DocumentForm
from pychorus import find_and_output_chorus


def validator(uploadFile):
    """
    验证文件大小和格式

    @param uploadFile: 文件对象
    """
    if uploadFile.size > 10485760:
        return False
    elif uploadFile.content_type not in ['audio/wav', 'audio/mp3']:
        return False
    else:
        return True


def index(request):
    """
    单应用首页—文件上传

    @param request: 请求对象
    """

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        # 文件是否正确及格式、大小验证
        if form.is_valid() and validator(request.FILES['docfile']):
            newdoc = Document(file=request.FILES['docfile'])
            newdoc.save()

            # 提取上传的文件路径及其名字和后缀
            filePath = newdoc.file.path.split('\\')
            NameExt = filePath[-1].split('.')

            # 音乐源文件地址
            input_path = '/'.join(filePath)
            # 生成音乐高潮部分的文件位置
            output_path = '/'.join(filePath[:-1])+'/'+NameExt[0]+'_high.wav'

            # 提取音乐高潮部分
            chorus_start_sec = find_and_output_chorus(input_path, output_path, 30)

            # 返回文件
            with open(output_path, 'rb') as f:
                response = HttpResponse(f)
                response['content_type'] = "application/octet-stream"
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(output_path)
                return response
    else:
        # 生成一个空表
        form = DocumentForm()
    # 渲染表单
    return render(request, 'index.html', {'form': form})


