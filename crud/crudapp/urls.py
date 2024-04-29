from django.urls import path
from . import views

urlpatterns = [
    path('item/', views.item_list, name='item_list'),
    path('new/', views.item_create, name='item_new'),
    path('edit/<int:pk>/', views.item_update, name='item_edit'),
    path('delete/<int:pk>/', views.item_delete, name='item_delete'),
    path('vendedor/', views.vendedor_list, name='vendedor_list'),
    path('nuevovendedor/', views.vendedor_create, name='vendedor_new'),
    path('editarvendedor/<int:pk>/', views.vendedor_update, name='vendedor_edit'),
    path('deletevendedor/<int:pk>/', views.vendedor_delete, name='vendedor_delete'),
]
