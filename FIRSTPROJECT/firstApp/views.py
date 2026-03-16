from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Student, Hobby
from .forms import StudentForm, HobbyForm

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




def createStudent(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read-students')

    context = {"form": form}
    return render(request, 'firstApp/form.html', context)


def readStudents(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, 'firstApp/students.html', context)


def readStudent(request, pk):
    student = Student.objects.get(id=pk)
    context = {"student": student}
    return render(request, 'firstApp/student.html', context)


def updateStudent(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('read-students')

    context = {"form": form}
    return render(request, 'firstApp/form.html', context)


def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('read-students')


# ---------------- HOBBY CRUD ----------------

def createHobby(request):
    form = HobbyForm()

    if request.method == 'POST':
        form = HobbyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read-hobbies')

    context = {"form": form}
    return render(request, 'firstApp/form.html', context)


def readHobbies(request):
    hobbies = Hobby.objects.all()
    context = {"hobbies": hobbies}
    return render(request, 'firstApp/hobby.html', context)


def readHobby(request, pk):
    hobby = Hobby.objects.get(id=pk)
    context = {"hobby": hobby}
    return render(request, 'firstApp/hobby.html', context)


def updateHobby(request, pk):
    hobby = Hobby.objects.get(id=pk)
    form = HobbyForm(instance=hobby)

    if request.method == 'POST':
        form = HobbyForm(request.POST, instance=hobby)
        if form.is_valid():
            form.save()
            return redirect('read-hobbies')

    context = {"form": form}
    return render(request, 'firstApp/form.html', context)


def deleteHobby(request, pk):
    hobby = Hobby.objects.get(id=pk)
    hobby.delete()
    return redirect('read-hobbies')