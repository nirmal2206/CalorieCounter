from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('food-list/',views.foodList, name='food_list'),
    path('food-list/<int:id>/add/', views.add, name='add'),
    path('food-list/<int:id>/remove/', views.remove, name='remove'),
    path('reset-calorie/', views.resetCalorie, name='reset_calorie')
]