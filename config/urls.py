from django.urls import path
from . import views

urlpatterns = [
    path('', views.mahsulot_list, name='mahsulot_list'),
    path('mahsulot/yangi/', views.mahsulot_create, name='mahsulot_create'),
    path('mahsulot/<int:pk>/tahrirlash/', views.mahsulot_update, name='mahsulot_update'),
    path('mahsulot/<int:pk>/ochirish/', views.mahsulot_delete, name='mahsulot_delete'),
]