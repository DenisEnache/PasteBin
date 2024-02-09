# pastebin/urls.py
# URL (Uniform Resource Locator) is a reference or address used to access resources on the internet.
# Naming URL patterns is a best practice in Django because it allows you to refer to the URL pattern elsewhere in your code, especially in templates.

from django.urls import path #path = function for defining URL routes in Django app
from . import views #views = functions for every URL logic

# URL routes and the associated views function
urlpatterns = [
    path('', views.home, name='home'), # app's start page 
    path('history/', views.history, name='history'), # defines a history page 
    path('texts/<int:pk>/', views.texts, name='texts'), 
    # texts/ = static part of URL(any URL matches this pattern must start with 'texts/')
    # <int:pk> = segment take an integer value from the URL and passes it as a parameter to the view function
    # int = specifies that the captured value should be converted to an integer
    # pk = primary key(the unique identifier for the database)
]

