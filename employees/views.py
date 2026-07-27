from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone

from accounts.models import User
from attendance.models import Attendance
from .models import Employee, Department
from .forms import EmployeeForm, EmployeeCreateForm


@login_required
# Afficher la liste de tous les employés (vue RH)
def employee_create(request):

    if request.method == "POST":

        form = EmployeeCreateForm(request.POST, request.FILES)

        if form.is_valid():

            # création du compte utilisateur
            user = User.objects.create_user(
                username=form.cleaned_data["email"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
                role="EMPLOYE"
            )

            user.first_name = form.cleaned_data["prenom"]
            user.last_name = form.cleaned_data["nom"]
            user.save()

            # création de l'employé
            employee = form.save(commit=False)

            employee.user = user

            employee.save()

            messages.success(
                request,
                "Employé créé avec succès."
            )

            return redirect("employee_list")

    else:

        form = EmployeeCreateForm()

    return render(
        request,
        "employees/employee_create.html",
        {
            "form": form
        }
    )

def employee_list(request):


    employees = Employee.objects.all()
    departments = Department.objects.all()

    department = request.GET.get("department")
    poste = request.GET.get("poste")
    statut = request.GET.get("statut")
    search = request.GET.get("search")

    if department:
        employees = employees.filter(department_id=department)

    if poste:
        employees = employees.filter(poste=poste)

    if statut:
        employees = employees.filter(statut=statut)

    if search:
        employees = employees.filter(
            Q(nom__icontains=search) |
            Q(prenom__icontains=search) |
            Q(email__icontains=search)
        )

    return render(request, "employees/employee_list.html", {
        "employees": employees,
        "departments": departments,
    })
    # Afficher les détails d’un employé spécifique
def employee_detail(request, pk):
# Récupère l’employé ou retourne une erreur 404 si introuvable
    employee = get_object_or_404(Employee, pk=pk)
 # Envoie l’employé au template de détail
    return render(request, "employees/employee_detail.html", {
        "employee": employee
    })
    
    
def employee_update(request, pk):

    employee = get_object_or_404(Employee, pk=pk)

    # formulaire pré-rempli avec données existantes
    form = EmployeeForm(request.POST or None, request.FILES or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('employee_list')

    return render(request, "employees/employee_form.html", {
        "form": form
    })
    
    
def employee_delete(request, pk):

    # Récupérer l'employé ou erreur 404
    employee = get_object_or_404(Employee, pk=pk)

    # Si confirmation envoyée (POST)
    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')

    # Sinon afficher page de confirmation
    return render(request, "employees/employee_confirm_delete.html", {
        "employee": employee
    })
    


def employee_dashboard(request):

    # récupérer l'employé connecté
    employee = get_object_or_404(Employee, user=request.user)

    # récupérer la présence du jour (si elle existe)
    today_attendance = Attendance.objects.filter(
        employee=employee,
        date=timezone.localdate()
    ).first()

    # envoyer les données au template
    return render(request, "employees/employee_dashboard.html", {
        "employee": employee,
        "attendance": today_attendance
    })
    
    
    # récupérer la présence du jour
