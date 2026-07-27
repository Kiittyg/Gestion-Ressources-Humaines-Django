from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        'matricule',
        'nom',
        'prenom',
        'email',
        'department',
        'poste',
        'type_contrat',
        'statut',
    )

    list_filter = (
        'department',
        'poste',
        'type_contrat',
        'statut',
    )

    search_fields = (
        'matricule',
        'nom',
        'prenom',
        'email',
    )

    ordering = ('-created_at',)

    readonly_fields = ('matricule', 'created_at')