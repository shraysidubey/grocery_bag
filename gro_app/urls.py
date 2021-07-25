from django.conf.urls import patterns, url
from gro_app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^grocery_details/$', views.grocery_details, name='grocery_details'),
        )