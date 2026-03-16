from django.forms import ModelForm
from .models import Student, Hobby


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class HobbyForm(ModelForm):
    class Meta:
        model = Hobby
        fields = '__all__'