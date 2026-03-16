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
    path('admin/',views.admin, name="admin"),
#    Student URLs
    path('create-student/', views.createStudent, name='create-student'),
    path('read-students/', views.readStudents, name='read-students'),
    path('read-student/<str:pk>/', views.readStudent, name='read-student'),
    path('update-student/<str:pk>/', views.updateStudent, name='update-student'),
    path('delete-student/<str:pk>/', views.deleteStudent, name='delete-student'),

    # Hobby URLs
    path('create-hobby/', views.createHobby, name='create-hobby'),
    path('read-hobbies/', views.readHobbies, name='read-hobbies'),
    path('read-hobby/<str:pk>/', views.readHobby, name='read-hobby'),
    path('update-hobby/<str:pk>/', views.updateHobby, name='update-hobby'),
    path('delete-hobby/<str:pk>/', views.deleteHobby, name='delete-hobby'),

]