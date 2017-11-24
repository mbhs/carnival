from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.about, name='about'),
    url(r'^instruments/$', views.instruments, name='instruments'),
    url(r'^organizers/$', views.organizers, name='organizers'),
]
