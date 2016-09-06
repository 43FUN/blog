from django import forms
from django.contrib.auth import forms as auth_forms
from users.models import User


class UserChangeForm(auth_forms.UserChangeForm):
    pass


class UserCreationForm(auth_forms.UserCreationForm):
    pass


class UploadFileForm(forms.Form):
    file = forms.FileField()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'avatar',
            'first_name',
            'last_name',
            'phone',
            'skype'
        ]
