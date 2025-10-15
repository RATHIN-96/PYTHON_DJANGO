from django import forms
from Newapp.models import employee

class Student(forms.Form):
    first_name = forms.CharField(max_length=30)
    second_name = forms.CharField(max_length=30)
    place = forms.CharField(max_length=50)
    age = forms.IntegerField()
    number = forms.IntegerField()

class empform(forms.ModelForm):
    class Meta:
        model= employee
        # fields = '__all__'
        fields = ['age','number']