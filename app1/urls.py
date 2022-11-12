from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tables/', views.tables, name='tables'),
    path('billing/', views.billing, name='billing'),
]
