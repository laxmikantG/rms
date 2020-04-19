from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),

    path('add', views.add_table, name='add_table'),
    path('modify/<table_id>', views.modify_table, name='modify_table'),
    path('remove/<table_id>', views.remove_table, name='remove_table'),

   path('menu/add', views.add_menu, name='add_menu'),
   path('menu/edit/<menu_id>', views.edit_menu, name='edit_menu'),
   path('menu/remove/<menu_id>', views.remove_menu, name='remove_menu'),

  #  path('orders/', views.orders, name='orders'),
   path('orders/order/', views.get_order, name='get_order'),
   path('orders/remove/<table_id>/<menu_id>', views.remove_orders, name='remove_orders'),


]
