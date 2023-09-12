from django.urls import path

from machineInfo import views

urlpatterns = [
    path('', views.home),
    path('items/<int:id>/', views.item)
]
