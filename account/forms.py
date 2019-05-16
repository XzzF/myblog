from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from .models import UserInfo


# 提交表单之后, 不会对数据库进行修改, 就继承 forms.Form
# 若将表单中的数据写入数据库或修改某些记录的值, 就继承 forms.ModelForm
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email")

    # 以 clean_XXX 方式命名的方法, 都会在调用 is_valid() 方法时执行
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords do not match!")
        return cd['password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone", "birth")


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school", "company", "profession", "address", "aboutme", "photo")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)
