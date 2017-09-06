#coding=utf-8
from django import forms
from django.forms import fields as Ffields
from django.forms import widgets as Fwidgets
from models import UserInfo

class UserInfoModelForm(forms.ModelForm):          #数据库表单

    is_rmb = Ffields.CharField(widget=Fwidgets.CheckboxInput())          # 额外字段像网页上的checkbox，一个月内免登陆，用提交到数据库么？这个只需要设置session和cookie就可以了。

    class Meta:    #Meta是一个内部类,它用于定义一些Django模型类的行为特性
        model = UserInfo
        fields = '__all__'
        # fields =  ['username','email']
        # exclude = ['username']
        labels = {
            'username': '用户名',
            'email': '邮箱',
        }
        help_texts = {
            'username': '！！！！'
        }
        widgets = {
            'username': Fwidgets.Textarea(attrs={'class': 'c1'})
        }
        error_messages = {
            '__all__':{    # 整体错误信息

            },
            'email': {
                'required': '邮箱不能为空',
                'invalid': '邮箱格式错误..',
            }
        }
        field_classes = {  # 定义字段的类是什么
            # 'email': Ffields.URLField  # 这里只能填类，加上括号就是对象了。
        }

        # localized_fields=('ctime',)  # 哪些字段做本地化

""" Form验证：
    UserInfoForm -> Form -> BaseForm( 包含is_valid等方法)

# ModelForm验证：
    UserInfoModelForm -> ModelForm -> BaseModelForm -> BaseForm"""


"""ModelForm
    a.  class Meta:
            model,                           # 对应Model的
            fields=None,                     # 字段
            exclude=None,                    # 排除字段
            labels=None,                     # 提示信息
            help_texts=None,                 # 帮助提示信息
            widgets=None,                    # 自定义插件
            error_messages=None,             # 自定义错误信息（整体错误信息from django.core.exceptions import NON_FIELD_ERRORS）
            field_classes=None               # 自定义字段类 （也可以自定义字段）
            localized_fields=('birth_date',) # 本地化，如：根据不同时区显示数据
            如：
                数据库中
                    2016-12-27 04:10:57
                setting中的配置
                    TIME_ZONE = 'Asia/Shanghai'
                    USE_TZ = True
                则显示：
                    2016-12-27 12:10:57
    b. 验证执行过程
        is_valid -> full_clean -> 钩子 -> 整体错误

    c. 字典字段验证
        def clean_字段名(self):
            # 可以抛出异常
            # from django.core.exceptions import ValidationError
            return "新值"
    d. 用于验证
        model_form_obj = XXOOModelForm()
        model_form_obj.is_valid()
        model_form_obj.errors.as_json()
        model_form_obj.clean()
        model_form_obj.cleaned_data
    e. 用于创建
        model_form_obj = XXOOModelForm(request.POST)
        #### 页面显示，并提交 #####
        # 默认保存多对多
            obj = form.save(commit=True)
        # 不做任何操作，内部定义 save_m2m（用于保存多对多）
            obj = form.save(commit=False)
            obj.save()      # 保存单表信息
            obj.save_m2m()  # 保存关联多对多信息

    f. 用于更新和初始化
        obj = model.tb.objects.get(id=1)
        model_form_obj = XXOOModelForm(request.POST,instance=obj)
        ...

        PS: 单纯初始化"""
    # model_form_obj = XXOOModelForm(initial={...})

"""
总结1. 生成HTML标签：class Meta: ...
    2. mf = xxxModelForm(instance=ModelObj) 生成默认值
    3. 额外的标签， is_rmb = Ffields.CharField(widget=Fwidgets.CheckboxInput())
    4. 各种验证 is_valid() -> 各种钩子...
    5.  mf.save()
        # 或
        instance = mf.save(False)
        instance.save()
        mf.save_m2m()"""


class FileUploadForm(forms.Form):  #创建表单
    my_file = forms.FileField()