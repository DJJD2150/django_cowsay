"""http_forms_and_cows_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from http_forms_and_cows_app.views import index_view, history_view

# Got help with VS Code terminal error from Joe Kaufeld and Peter Marsh in study hall.
urlpatterns = [
    path('', index_view, name="homepage"),
    path('history/', history_view, name="historyview"),
    path('admin/', admin.site.urls),
]
