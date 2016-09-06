# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from users.forms import UserForm
from article.models import Article
# Create your views here.


def profile(request):
    form = UserForm(request.POST or None,
                    request.FILES or None,
                    instance=request.user)
    args = {}
    args['form'] = form
    args['article'] = Article.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    return render(request, 'profile.html', args)




