from dataclasses import fields
from re import L
from tkinter import Widget
from django import forms
from .models import Student, Track
#auth import
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fname', 'lname', 'age', 'student_track')
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'student_track': forms.Select(attrs={'class': 'form-control'}),
        }
        
class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('track_name',)


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        # fields = ('__all__')
        