from django.urls import path
from . import views

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),
    path('create/', views.transaction_create, name='transaction_create'),
    path('edit/<int:pk>/', views.transaction_edit, name='transaction_edit'),
    path('delete/<int:pk>/', views.transaction_delete, name='transaction_delete'),

    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),

    path('status/', views.status_list, name='status_list'),
    path('status/create/', views.status_create, name='status_create'),
    path('status/edit/<int:pk>/', views.status_edit, name='status_edit'),
    path('status/delete/<int:pk>/', views.status_delete, name='status_delete'),

    path('type/', views.type_list, name='type_list'),
    path('type/create/', views.type_create, name='type_create'),
    path('type/edit/<int:pk>/', views.type_edit, name='type_edit'),
    path('type/delete/<int:pk>/', views.type_delete, name='type_delete'),

    path('category/', views.category_list, name='category_list'),
    path('category/create/', views.category_create, name='category_create'),
    path('category/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('category/delete/<int:pk>/', views.category_delete, name='category_delete'),

    path('subcategory/', views.subcategory_list, name='subcategory_list'),
    path('subcategory/create/', views.subcategory_create, name='subcategory_create'),
    path('subcategory/edit/<int:pk>/', views.subcategory_edit, name='subcategory_edit'),
    path('subcategory/delete/<int:pk>/', views.subcategory_delete, name='subcategory_delete'),

    path('dictionary/', views.dictionary_management, name='dictionary_management'),
]

