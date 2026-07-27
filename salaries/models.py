from django.db import models
from employees.models import Employee
from attendance.models import Attendance


class Salary(models.Model):

    # employé concerné
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    # liste des mois
    MONTH_CHOICES = [
        
        (1, "Janvier"),
        (2, "Février"),
        (3, "Mars"),
        (4, "Avril"),
        (5, "Mai"),
        (6, "Juin"),
        (7, "Juillet"),
        (8, "Août"),
        (9, "Septembre"),
        (10, "Octobre"),
        (11, "Novembre"),
        (12, "Décembre"),
    ]

    # mois du salaire
    month = models.IntegerField(
        choices=MONTH_CHOICES
    )

    # année
    year = models.IntegerField()

    # salaire de base
    base_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
# prime
    bonus = models.DecimalField(
        "Prime",
        max_digits=10,
        decimal_places=2,
        default=0
    )
    # retenues
    deductions = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    # salaire net
    net_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    # date de création
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        # récupérer les absences du mois concerné
        absences = Attendance.objects.filter(
            employee=self.employee,
            status="absent",
            date__month=self.month,
            date__year=self.year
        ).count()

        # retenue par jour d'absence
        deduction_per_day = 100

        # calcul des retenues
        self.deductions = absences * deduction_per_day

        # récupération du salaire de base
        self.base_salary = self.employee.salaire

        # calcul du salaire net
        self.net_salary = (
        self.base_salary
        + self.bonus
        - self.deductions
    )

        super().save(*args, **kwargs)

    def __str__(self):

        return (
            f"{self.employee.nom} - "
            f"{self.get_month_display()} {self.year}"
        )