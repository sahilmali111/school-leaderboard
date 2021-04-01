"""school_task URL Configuration

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
from App import views
from django.views.static import serve
from django.conf.urls import url

from school_task import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('student', views.student_api, name="student_api"),
    path('student_data', views.student_data, name="student_data"),
    path('leaderboard_api', views.leaderboard_api, name="leaderboard_api"),
    path('leaderboard', views.leaderboard, name="leaderboard"),
    # url(r'^media/(?p<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
    # url(r'^static/(?p<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
]
