from django.urls import path
from . import views

urlpatterns = [
    
    path('home',views.get_home_page,name='home'),
    path('addCar',views.add_car,name='addCar'),
    path('carDetails/<int:car_id>',views.get_details,name='carDetails'),
    path('delete/<int:car_id>',views.delete_car),
    path('update/<int:car_id>',views.update_car),
    path('reservations',views.get_reservations,name='reservations'),
    path('search',views.search_for_car,name='search')

    
]
