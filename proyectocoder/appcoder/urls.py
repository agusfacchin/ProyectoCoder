from django.urls import path
from appcoder import views

urlpatterns= [

   path("", views.inicio, name="Inicio"),  
   path('restaurante', views.restaurante, name="Restaurante"),
   path('empleados', views.empleados, name="Empleados"),
   path('platos', views.platos, name="Platos"),
   path('buscar/', views.buscar),

]

