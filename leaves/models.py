
from django.db import models
from employees.models import Employee


class Leave(models.Model):

    # employé qui demande le congé
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    # date de début du congé
    start_date = models.DateField()

    # date de fin du congé
    end_date = models.DateField()

    # raison du congé
    reason = models.TextField()

    # statut de la demande
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "En attente"),
            ("approved", "Approuvé"),
            ("rejected", "Refusé")
        ],
        default="pending"
    )

    # date de création de la demande
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        # affichage dans l'administration
        return f"{self.employee.nom} - {self.status}"