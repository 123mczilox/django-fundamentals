from django.urls import path
from . import views

urlpatterns = [
     path('',views.home, name="home"),
    path('home/',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('contacts/',views.contacts, name="contacts"),
    path('bookings/',views.bookings, name="bookings"),
    path('homed/',views.homed, name="homed"),
    path('admin/',views.admin, name="admin")

    
]