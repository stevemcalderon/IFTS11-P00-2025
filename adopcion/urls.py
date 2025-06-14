from django.urls import path
from . import views

urlpatterns = [
    path('perros/', views.lista_perros, name='lista_perros'),
    path('adoptar/', views.postular_adopcion, name='postular_adopcion'),
]

path('historial/<str:dni>/', views.historial_adopciones, name='historial_adopciones'),
