from django.conf.urls import url

from . import views

app_name = 'validation'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^confirmpin/$', views.verify, name='verify'),
    url(r'^loginpage/$', views.confirmpin, name='confirmpin'),
    #url(r'^loginpage/$', views.loginpage, name='loginpage'),
]
