from django import forms
from .models import Salary


class SalaryForm(forms.ModelForm):

    class Meta:

        model = Salary

        fields = [
            "employee",
            "month",
            "year",
            "bonus",
        ]

        widgets = {

            "employee": forms.Select(),

            "month": forms.Select(),

            "year": forms.NumberInput(attrs={
                "placeholder": "Ex : 2026"
            }),

            "bonus": forms.NumberInput(attrs={
                "placeholder": "Prime en FCFA"
            }),

        }