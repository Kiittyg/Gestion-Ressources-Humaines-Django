from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from datetime import time
from django.shortcuts import redirect, get_object_or_404
from .models import Attendance
from employees.models import Employee


def check_in(request):

    # récupérer l'employé connecté
    employee = Employee.objects.get(user=request.user)

    # récupérer ou créer la présence du jour
    attendance, created = Attendance.objects.get_or_create(
        employee=employee,
        date=timezone.localdate()
    )

    # empêcher un deuxième pointage d'arrivée
    if attendance.check_in:
        return redirect("employee_dashboard")

    # récupérer l'heure actuelle
    now = timezone.localtime().time()

    # enregistrer l'heure d'arrivée
    attendance.check_in = now

    # heure limite d'arrivée (10h00)
    ATTENDANCE_LIMIT = time(10, 0)

    # déterminer le statut
    if now > ATTENDANCE_LIMIT:
        attendance.status = "late"
    else:
        attendance.status = "present"

    # sauvegarder dans la base de données
    attendance.save()

    return redirect("employee_dashboard")


def check_out(request):

    # récupérer l'employé connecté
    employee = get_object_or_404(Employee, user=request.user)

    # récupérer la présence du jour
    attendance = Attendance.objects.get(
        employee=employee,
        date=timezone.localdate()
    )

    # empêcher le départ sans arrivée
    if not attendance.check_in:
        return redirect("employee_dashboard")

    # empêcher un deuxième pointage de départ
    if attendance.check_out:
        return redirect("employee_dashboard")

    # enregistrer l'heure de sortie
    attendance.check_out = timezone.localtime().time()

    # sauvegarder dans la base de données
    attendance.save()

    return redirect("employee_dashboard")

def attendance_list(request):

    # récupérer la date choisie dans l'URL
    selected_date = request.GET.get("date")

    # si aucune date n'est choisie
    if selected_date:

        # afficher les présences de cette date
        attendances = Attendance.objects.filter(
            date=selected_date
        )

    else:

        # afficher les présences du jour
        attendances = Attendance.objects.filter(
            date=timezone.localdate()
        )

    return render(request, "attendance/attendance_list.html", {
        "attendances": attendances,
        "selected_date": selected_date
    })
    
def generate_absences(request):

    # récupérer la date du jour
    today = timezone.localdate()

    # récupérer tous les employés
    employees = Employee.objects.all()

    # parcourir tous les employés
    for employee in employees:

        # vérifier s'il existe déjà une présence
        attendance = Attendance.objects.filter(
            employee=employee,
            date=today
        ).first()

        # si aucune présence n'existe
        if attendance is None:

            # créer une absence
            Attendance.objects.create(
                employee=employee,
                date=today,
                status="absent"
            )

    return redirect("attendance_list")