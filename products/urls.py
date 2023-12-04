from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_collectables, name='collectables'),
    path('<int:collectable_id>/', views.collectable_detail, name='collectable_detail'),
    path('add/', views.add_collectable, name='add_collectable'),
    path('sell_collectable/', views.sell_collectable, name='sell_collectable'),
    path('edit/<int:collectable_id>/', views.edit_collectable, name='edit_collectable'),
    path('delete/<int:collectable_id>/', views.delete_collectable, name='delete_collectable'),
]

