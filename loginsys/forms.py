from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserCreateForm(UserCreationForm):
    username = forms.EmailField(
        required=True, widget=forms.widgets.EmailInput(
            attrs={'placeholder': 'Email'})
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
