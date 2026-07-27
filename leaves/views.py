
# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404

from employees.models import Employee
from .models import Leave
from .forms import LeaveForm


def leave_request(request):

    # récupérer l'employé connecté
    employee = Employee.objects.get(
        user=request.user
    )

    # créer le formulaire
    form = LeaveForm(
        request.POST or None
    )

    # si le formulaire est valide
    if form.is_valid():

        # créer le congé sans sauvegarder
        leave = form.save(commit=False)

        # associer l'employé connecté
        leave.employee = employee

        # sauvegarder dans la base
        leave.save()

        return redirect(
            "employee_dashboard"
        )

    return render(
        request,
        "leaves/leave_form.html",
        {
            "form": form
        }
    )
def employee_leave_list(request):

    # récupérer l'employé connecté
    employee = get_object_or_404(
        Employee,
        user=request.user
    )

    # récupérer uniquement ses demandes
    leaves = Leave.objects.filter(
        employee=employee
    ).order_by("-created_at")

    return render(
        request,
        "leaves/employee_leave_list.html",
        {
            "leaves": leaves
        }
    )
    
    # =========================
# Liste des demandes de congé
# =========================
def leave_list(request):

    # récupérer toutes les demandes
    leaves = Leave.objects.all().order_by("-created_at")

    return render(request, "leaves/leave_list.html", {
        "leaves": leaves
    })
    
    
# =========================
# Accepter une demande
# =========================
def approve_leave(request, pk):

    # récupérer la demande ou erreur 404
    leave = get_object_or_404(Leave, pk=pk)

    # changer le statut
    leave.status = "approved"

    # sauvegarder
    leave.save()

    return redirect("leave_list")


# =========================
# Refuser une demande
# =========================
def reject_leave(request, pk):

    # récupérer la demande ou erreur 404
    leave = get_object_or_404(Leave, pk=pk)

    # changer le statut
    leave.status = "rejected"

    # sauvegarder
    leave.save()

    return redirect("leave_list")