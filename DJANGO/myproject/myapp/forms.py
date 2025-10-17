from django import forms
from myapp.models import Employee


class StudForm(forms.Form):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=30)
    place=forms.CharField(max_length=50)
    age=forms.IntegerField()

class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
    
        fields = '__all__'

        # fields = ['age','first_name']

        # exclude=['age']
      