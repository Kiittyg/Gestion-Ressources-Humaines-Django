
from django import forms
from .models import Leave
class LeaveForm(forms.ModelForm):

    class Meta:
        model = Leave
        fields = [
            "start_date",
            "end_date",
            "reason",
        ]

        widgets = {
            "start_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),

            "end_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),

            "reason": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Précisez le motif de votre demande...",
                    "class": "form-control",
                }
            ),
        }