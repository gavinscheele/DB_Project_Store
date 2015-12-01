"""Store URL Configuration

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
from welcome import views
welcome_view = views;
from store_user import views
store_user_view = views;


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', welcome_view.welcome, name="welcome"),
    url(r'^store_user/', store_user_view.store_user, name="store_user"),
    url(r'^store_user_signup/', store_user_view.store_user_signup, name="store_user_signup")
]
