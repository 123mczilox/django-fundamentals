from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('home/',views.home, name="home"),
    path('find_homes/',views.find_homes, name="find_homes"),
    path('bookings/',views.bookings, name="Bookings"),
    path('events/',views.events, name="events"),
    path('donations/', views.donations, name='Donations'),
    path('homed/',views.homed, name="homed"),
    path('admin/',views.admin, name="admin")
]