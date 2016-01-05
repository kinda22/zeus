# coding: utf-8
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserFormAdd(forms.Form):
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
    username = forms.CharField(required=True, max_length=20,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "用户名"}), error_messages={'required': '用户名不能为空'})
    email = forms.EmailField(required=False, max_length=20,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "邮箱"}), error_messages={'required': '邮箱不能为空','validate_email': '邮件格式不正确'})
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码" }), error_messages={'required': '密码不能为空'})
    password_confirm = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "确认密码" }), error_messages={'required': '确认密码不能为空'})

    fullname = forms.CharField(required=False,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "姓名"}))
    gender = forms.ChoiceField(required=False,choices=GENDER_CHOICES,widget=forms.RadioSelect(attrs={"class": "form-control"}))
    tel = forms.CharField(required=False,max_length=20,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "电话"}))
    mobile = forms.CharField(required=False,max_length=20,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "手机"}))
    address = forms.CharField(required=False,max_length=200,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "通讯地址"}))
    QQ = forms.CharField(required=False,max_length=20,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "QQ"}))
    position = forms.CharField(required=False,max_length=20,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "所在地"}))
    native = forms.CharField(required=False,max_length=20,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "籍贯"}))
    is_active = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "colored-warning"}))


class UserFormEdit(ModelForm):
#class UserFormEdit(forms.Form):
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
    email = forms.EmailField(required=False, max_length=20,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "邮箱"}), error_messages={'required': '邮箱不能为空','validate_email': '邮件格式不正确'})

    fullname = forms.CharField(required=False,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "姓名"}))
    gender = forms.ChoiceField(required=False,choices=GENDER_CHOICES,widget=forms.RadioSelect(attrs={"class": "form-control colored-blueberry"}))
    tel = forms.CharField(required=False,max_length=20,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "电话"}))
    mobile = forms.CharField(required=False,max_length=20,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "手机"}))
    address = forms.CharField(required=False,max_length=200,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "通讯地址"}))
    QQ = forms.CharField(required=False,max_length=20,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "QQ"}))
    position = forms.CharField(required=False,max_length=20,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "所在地"}))
    native = forms.CharField(required=False,max_length=20,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "籍贯"}))
    is_active = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "colored-success"}))
     
    class Meta:
        model = User
        fields = ['username','email','fullname','gender'] 
