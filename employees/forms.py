from django import forms
from .models import Employee
from accounts.models import User


# =========================
# FORMULAIRE EMPLOYÉ
# =========================
class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee

        # on prend tous les champs sauf ceux qu'on ne veut pas afficher
        fields = [
            'user',
            'nom',
            'prenom',
            'email',
            'telephone',
            'adresse',
            'date_naissance',
            'photo',
            'etat_civil',
            'poste',
            'niveau',
            'department',
            'type_contrat',
            'date_embauche',
            'salaire',
            'statut',
            'cv',
            'diplome',
            'contact_urgence',
        ]
        
        labels = {
            "nom": "Nom",
            "prenom": "Prénom",
            "email": "Email",
            "telephone": "Téléphone",
            "adresse": "Adresse",
            "date_naissance": "Date de naissance",
            "etat_civil": "État civil",
            "photo": "Photo",
            "poste": "Poste",
            "niveau": "Niveau",
            "department": "Département",
            "type_contrat": "Type de contrat",
            "date_embauche": "Date d'embauche",
            "salaire": "Salaire",
            "statut": "Statut",
            "cv": "Curriculum Vitae (CV)",
            "diplome": "Diplôme(s)",
            "contact_urgence": "Contact d'urgence",
}



class EmployeeCreateForm(forms.ModelForm):

   

    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput()
    )

    confirm_password = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput()
    )

    class Meta:
        model = Employee

        exclude = (
            "user",
            "matricule",
            "created_at",
        )

        widgets = {

            "nom": forms.TextInput(),

            "prenom": forms.TextInput(),

            "email": forms.EmailInput(),

            "telephone": forms.TextInput(),

            "adresse": forms.Textarea(attrs={
                "rows": 3
            }),

            "date_naissance": forms.DateInput(attrs={
                "type": "date"
            }),

            "etat_civil": forms.Select(),

            "poste": forms.Select(),
            "niveau":forms.Select(),
            "department": forms.Select(),

            "type_contrat": forms.Select(),

            "date_embauche": forms.DateInput(attrs={
                "type": "date"
            }),

            "salaire": forms.NumberInput(),

            "statut": forms.TextInput(),

            "photo": forms.ClearableFileInput(),

            "cv": forms.ClearableFileInput(),

            "diplome": forms.ClearableFileInput(),

            "contact_urgence": forms.Textarea(attrs={
                "rows": 2
            }),

        }

    def clean(self):

        cleaned_data = super().clean()

        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(
                "Les mots de passe ne correspondent pas."
            )

       

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Cette adresse e-mail existe déjà."
            )

        return cleaned_data