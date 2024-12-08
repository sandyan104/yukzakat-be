from django.urls import path
from . import views

urlpatterns = [
    path('', views.akun_list, name='akun-list'),
    path('edit/', views.akun_edit, name='akun-edit'),
    path('delete/', views.akun_delete, name='akun-delete'),
    path('create/', views.akun_create, name='akun-create')
]
