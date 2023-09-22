from django.urls import path

from project_beginner_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]