# mypastebin/urls.py

from django.urls import path, include # include = used for including URL routes from other Django apps in the main project

urlpatterns = [
    path('', include('pastebin.urls')), #includes all URL routes defined in pastebin/urls.py. When path is empty Django will search in that list
]

