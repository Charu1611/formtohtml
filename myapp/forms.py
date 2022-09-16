from django.db import models  
from django.forms import fields  
# from .models import UploadImage  
from django import forms  
from .models import UploadTemplate

class UploadTemplateForm(forms.ModelForm):
    class Meta:
        model=UploadTemplate
        fields=("email","phone","city","dob","education","photo","template")

