"""freyja URL Configuration

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

import freyja.views as core_views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', core_views.IndexView.as_view(), name='index'),
    url(r'^about$', core_views.AboutView.as_view(), name='about'),
    url(r'^signup$', core_views.signup, name='signup'),
    url(r'^login$', core_views.login, name='login'),  
    url(r'^logout$', core_views.logout, name='logout'),
    url(r'^forget$', core_views.forget, name='forget'),
    url(r'^reset_password$', core_views.reset_password, name='reset_password'),
]
