from django.contrib import admin

# Register your models here.
# coding: utf-8

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users import models, forms


@admin.register(models.User)
class UserAdmin(UserAdmin):
    form = forms.UserChangeForm
    add_form = forms.UserCreationForm

    fieldsets = (
        (None, {'fields': (
            'username',
            'password'
        )}),
        ('Персональная информация', {'fields': (
            'avatar',
            'first_name',
            'last_name',
            'email',
            'phone',
            'skype'
        )}),
        ('Статус', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
        )}),
        ('Даты входа', {'fields': (
            'last_login',
            'date_joined'
        )}),
    )