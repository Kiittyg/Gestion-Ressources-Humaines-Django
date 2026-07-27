from django.urls import path
from . import views

urlpatterns = [

    # créer un salaire
    path(
        "create/",views.salary_create,name="salary_create"
    ),

    # liste des salaires
    path(
        "list/", views.salary_list,name="salary_list"
    ),
    path("my-salaries/",views.employee_salary_list,name="employee_salary_list"
),
    path( "detail/<int:pk>/", views.salary_detail, name="salary_detail"
),
    path("pdf/<int:pk>/",views.salary_pdf, name="salary_pdf"
),
path("<int:pk>/update/", views.salary_update, name="salary_update"),
path("<int:pk>/delete/", views.salary_delete, name="salary_delete"),
]