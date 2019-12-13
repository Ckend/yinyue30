from django import forms


class DocumentForm(forms.Form):
    """
    用于生成表单的类
    @param forms.Form: 继承表单类
    """

    # label和help_text属性都可以在前端中被调取
    docfile = forms.FileField(
        label='选择文件',
        help_text='最大 10 m'
    )
