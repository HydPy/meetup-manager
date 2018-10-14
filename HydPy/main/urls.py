from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addUser', views.add_user, name='add_user'),
    path('addSpeaker', views.add_speaker, name='add_speaker'),
    re_path(r'^user/(?P<username>\w{1,32})/$', views.get_user, name='get_user'),
]
