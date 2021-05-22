from django import forms
from .models import *

class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = "__all__"