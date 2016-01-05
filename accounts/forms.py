# coding: utf-8
from django import forms

class AccountLoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=20,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "用户名"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码" }))

class AccountRegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=20,widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "用户名"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码" }))
    password_confirm = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "确认密码" })) 
