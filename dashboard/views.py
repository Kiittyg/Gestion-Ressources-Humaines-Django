
# Create your views here.
from django.shortcuts import render
from employees.models import Employee
from departments.models import Department


# =========================
# DASHBOARD RH
# =========================
def dashboard_home(request):

    # Nombre total d'employés
    total_employees = Employee.objects.count()

    # Employés actifs
    active_employees = Employee.objects.filter(statut="actif").count()

    # Tous les départements
    departments = Department.objects.all()

    # Construction stats par département
    dept_stats = []

    for dept in departments:
        count = Employee.objects.filter(department=dept).count()
        dept_stats.append({
            "department": dept.name,
            "count": count
        })

    return render(request, "dashboard/home.html", {
        "total_employees": total_employees,
        "active_employees": active_employees,
        "dept_stats": dept_stats
    })