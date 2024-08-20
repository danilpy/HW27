from django.contrib import admin
from django.urls import path

from vacancies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('vacancy/', views.index),
]
