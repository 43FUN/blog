from django.conf.urls import url, include

"""firstapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from article import views
urlpatterns = [
    url(r'^articles/all/$', views.articles, name='articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$',
        views.article, name='article'),
    url(r'^articles/addlike/(?P<article_id>\d+)/$',
        views.addlike, name='addlike'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$',
        views.addcomment, name='addcomment'),
    url(r'^page/(\d+)/$', views.articles, name='articles'),
    url(r'^articles/article_add/0/$',
        views.article_add, name='article_add'),
    url(r'^articles/delete/(?P<article_id>\d+)/$',
        views.delete, name='delete'),
    url(r'^articles/article_edit/(?P<article_id>\d+)/$',
        views.article_edit, name='article_edit'),
    url(r'^$', views.articles, name='articles'),


]
