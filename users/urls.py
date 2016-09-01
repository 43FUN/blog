from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^profile', views.profile, name='profile'),
]