from django.forms import ModelForm
from .models import Student, Hobby , ChildrenHome


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class HobbyForm(ModelForm):
    class Meta:
        model = Hobby
        fields = '__all__'


class ChildrenHomeForm(ModelForm):
    class Meta:
        model = ChildrenHome
        fields = '__all__'