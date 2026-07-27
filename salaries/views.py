
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Salary
from .forms import SalaryForm
from employees.models import Employee



def salary_create(request):

    form = SalaryForm(request.POST or None)

    if form.is_valid():

        salary = form.save()

        return redirect("salary_list")

    return render(request, "salaries/salary_form.html", {
        "form": form
    })
    
    # =========================
# Modifier un salaire
# =========================
def salary_update(request, pk):

    salary = get_object_or_404(
        Salary,
        pk=pk
    )

    form = SalaryForm(
        request.POST or None,
        instance=salary
    )

    if form.is_valid():

        form.save()

        return redirect("salary_list")

    return render(
        request,
        "salaries/salary_form.html",
        {
            "form": form
        }
    )
    # =========================
# Supprimer un salaire
# =========================
def salary_delete(request, pk):

    salary = get_object_or_404(
        Salary,
        pk=pk
    )

    if request.method == "POST":

        salary.delete()

        return redirect("salary_list")

    return render(
        request,
        "salaries/salary_confirm_delete.html",
        {
            "salary": salary
        }
    )
def salary_list(request):

    # récupérer tous les salaires
    salaries = Salary.objects.all().order_by(
        "-year",
        "-month"
    )

    return render(request, "salaries/salary_list.html", {
        "salaries": salaries
    })
    
    
# =========================
# Salaires de l'employé connecté
# =========================
def employee_salary_list(request):

    # récupérer l'employé connecté
    employee = get_object_or_404(
    Employee,
    user=request.user
)

    # récupérer ses salaires
    salaries = Salary.objects.filter(
        employee=employee
    ).order_by(
        "-year",
        "-month"
    )

    return render(
        request,
        "salaries/employee_salary_list.html",
        {
            "salaries": salaries
        }
    )
    
# =========================
# Détail d'un bulletin
# =========================
def salary_detail(request, pk):

    # récupérer le salaire
    salary = get_object_or_404(
        Salary,
        pk=pk
    )
   # si l'utilisateur est un employé
    if request.user.role != "RH":

    # récupérer son employé
     employee = get_object_or_404(
        Employee,
        user=request.user
    )

    # vérifier que le bulletin lui appartient
    if salary.employee != employee:
         return redirect("employee_salary_list")
    return render(
        request,
        "salaries/salary_detail.html",
        {
            "salary": salary
        }
    )    
    
# =========================
# Télécharger le bulletin PDF
# =========================
@login_required
def salary_pdf(request, pk):

    # récupérer le salaire
    salary = get_object_or_404(
        Salary,
        pk=pk
    )

    # création de la réponse PDF
    response = HttpResponse(
        content_type="application/pdf"
    )

    response[
        "Content-Disposition"
    ] = (
        f'attachment; filename="bulletin_{salary.id}.pdf"'
    )

    # créer le document PDF
    pdf = canvas.Canvas(response)

    # titre
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, 800, "BULLETIN DE SALAIRE")

    # informations
    pdf.setFont("Helvetica", 12)

    pdf.drawString(
        50,
        740,
        f"Employé : {salary.employee.prenom} {salary.employee.nom}"
    )

    pdf.drawString(
        50,
        710,
        f"Mois : {salary.get_month_display()} {salary.year}"
    )

    pdf.drawString(
    50,
    680,
    f"Salaire de base : {salary.base_salary} FCFA"
)

    pdf.drawString(
    50,
    650,
    f"Prime : {salary.bonus} FCFA"
)

    pdf.drawString(
    50,
    620,
    f"Retenues : {salary.deductions} FCFA"
)

    pdf.drawString(
    50,
    590,
    f"Salaire net : {salary.net_salary} FCFA"
)

    # sauvegarder le PDF
    pdf.save()

    return response