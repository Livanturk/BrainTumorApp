from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path("upload/", views.upload_and_predict, name = "upload_and_predict"),

]
