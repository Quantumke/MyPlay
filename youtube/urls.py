"""youtube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from clone import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^watch/(?P<slug>[^\.]+).html', views.view_more, name='view_more'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<slug>[\w\-]+)/$', views.view_more, name="vidz"),
    url('^english.html/', views.english, name='english'),
    url('^chinese.html/', views.chinese, name='chinese'),
    url('^hindi.html/', views.hindi, name='hindi'),
    url('^animation.html/', views.animation, name='animation'),

]
