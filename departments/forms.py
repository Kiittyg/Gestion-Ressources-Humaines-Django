from django import forms
from .models import Department


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department

        fields = [
            "name",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Nom du département"
            }),
        }