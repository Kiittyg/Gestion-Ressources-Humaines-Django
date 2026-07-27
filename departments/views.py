
from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from .forms import DepartmentForm


# ============================
# Liste des départements
# ============================
def department_list(request):

    departments = Department.objects.all().order_by("name")

    return render(
        request,
        "departments/department_list.html",
        {
            "departments": departments
        }
    )


# ============================
# Ajouter un département
# ============================
def department_create(request):

    if request.method == "POST":

        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("department_list")

    else:

        form = DepartmentForm()

    return render(
        request,
        "departments/department_form.html",
        {
            "form": form,
            "title": "Ajouter un département"
        }
    )


# ============================
# Modifier un département
# ============================
def department_update(request, pk):

    department = get_object_or_404(
        Department,
        pk=pk
    )

    form = DepartmentForm(
        request.POST or None,
        instance=department
    )

    if form.is_valid():

        form.save()

        return redirect("department_list")

    return render(
        request,
        "departments/department_form.html",
        {
            "form": form,
            "title": "Modifier un département"
        }
    )


# ============================
# Supprimer un département
# ============================
def department_delete(request, pk):

    department = get_object_or_404(
        Department,
        pk=pk
    )

    if request.method == "POST":

        department.delete()

        return redirect("department_list")

    return render(
        request,
        "departments/department_confirm_delete.html",
        {
            "department": department
        }
    )