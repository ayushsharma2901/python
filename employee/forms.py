from django import forms
from django.forms import ModelForm
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group,GroupManager
from django.db.models import Q

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        
        fields = ('emp_name', 'emp_email', 'emp_contact', 'emp_role', 'emp_salary', 'image')

        widgets = {
            'emp_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'emp_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'emp_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact No.'}),
            'emp_role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Role'}),
            'emp_salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class RegisterGroup(ModelForm):
    
    class Meta:
        model = Group
        fields = ["name"]


class EditGroup(ModelForm):

        # Users=forms.ModelChoiceField(queryset=User.objects.filter(groups__isnull=True))
        Users=forms.ModelChoiceField(queryset=User.objects.filter(groups__isnull=True))
        class Meta: 
            model=Group
            fields=["name","Users"]

class AddPersonnelToGroupForm(forms.Form):
    personnels = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.SelectMultiple(attrs={"class" : "form-control select-multiple"}))
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.Select(attrs={"class" : "form-control select-multiple"})
    )
