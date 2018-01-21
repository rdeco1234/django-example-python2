from django.conf.urls import include, url
from app.views import contact
from django.contrib import admin

urlpatterns = [
    url(r'^mail/', contact),
]
