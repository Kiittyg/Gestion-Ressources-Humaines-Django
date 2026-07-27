from django.db import models
from datetime import time,datetime
from employees.models import Employee


class Attendance(models.Model):

    # lien avec l'employé
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    # date du pointage (jour automatique)
    date = models.DateField(auto_now_add=True)

    # heure d'arrivée
    check_in = models.TimeField(null=True, blank=True)

    # heure de départ
    check_out = models.TimeField(null=True, blank=True)

    # statut de présence
    status = models.CharField(
        max_length=20,
        choices=[
            ('present', 'Present'),
            ('absent', 'Absent'),
            ('late', 'Late'),
        ],
        default='present'
    )

    # heure limite d'arrivée (ex: 09h00)
    ATTENDANCE_LIMIT = time(9, 0)

    # sauvegarde automatique
    def save(self, *args, **kwargs):

        # si l'employé n'a pas pointé ou est en retard
        if self.check_in:

            # retard si arrivée après 9h00
            if self.check_in > self.ATTENDANCE_LIMIT:
                self.status = "late"
            else:
                self.status = "present"

        else:
            # si pas de check-in → absent
            self.status = "absent"

        super().save(*args, **kwargs)

    
    
    def worked_hours(self):

        # si pas de check-in ou check-out → impossible de calculer
        if not self.check_in or not self.check_out:
            return 0

        # convertir en datetime complet pour calcul
        check_in_datetime = datetime.combine(self.date, self.check_in)
        check_out_datetime = datetime.combine(self.date, self.check_out)

        # calcul de la durée totale
        duration = check_out_datetime - check_in_datetime

        # retour en heures
        return duration.total_seconds() / 3600

    def __str__(self):
        return f"{self.employee.prenom} {self.employee.nom} - {self.date}"