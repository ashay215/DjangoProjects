from django.conf.urls import url

from . import views

app_name = 'validation'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^confirmpin/$', views.verify, name='verify'),
    url(r'^loginpage/$', views.confirmpin, name='confirmpin'),
    url(r'^login/$', views.login, name='login'),
    url(r'^retrieval/$', views.retrieval, name='retrieval'),
]
