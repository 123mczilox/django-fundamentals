from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# def home(response):
#     return HttpResponse("habari softare developers")
# home(HttpResponse)

# def about(response):
#     return HttpResponse("LEARN MORE ABOUT GALLEON TECHNOLOGIES")
# about(HttpResponse)

# def contacts(response):
#     return HttpResponse("FELL FREE TO CONTACT US")
# contacts(HttpResponse)

def home(request):
    context = {"data": "Welcome to Galleon Technologies"}
    return render(request, 'main.html', context)


def find_homes(request):
    context = {"data": "Learn more about Galleon Technologies"}
    return render(request, 'firstApp/find_homes.html', context)

def bookings(request):
    context = {"data": "Manage your bookings"}
    return render(request, 'firstApp/bookings.html', context)
def events(request):
    context = {"data": "Explore our events"}
    return render(request, 'firstApp/events.html', context)

def donations(request):
    context = {"data": "Support our cause"}
    return render(request, 'firstApp/donations.html', context)

def homed(request):
    context = {"data": "Welcome to your dashboard"}
    return render(request, 'firstApp/homed.html', context)

def admin(request):
    context = {"data": "Admin panel"}
    return render(request, 'firstApp/admin.html', context)
