from django import forms
from.models import *




class studentModelForm(forms.ModelForm):
    class Meta:
        model=studentModel
        fields="__all__"
        widget={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "age":forms.TextInput(attrs={"class":"form-control"}),
            "gaurdian_name":forms.TextInput(attrs={"class":"form-control"}),
            "total_marks":forms.NumberInput(attrs={"class":"form-control"}),
        }
       
