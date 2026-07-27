from . import views
from .views import employee_list,employee_detail,employee_update,employee_delete
from django.urls import path
urlpatterns = [
   path("list/", employee_list, name="employee_list"),
     # Page détail d’un employé (ID dynamique)
   path("detail/<int:pk>/", employee_detail, name="employee_detail"),
   path("update/<int:pk>/", employee_update, name="employee_update"),
   path("delete/<int:pk>/", employee_delete, name="employee_delete"),
  path("dashboard/", views.employee_dashboard, name="employee_dashboard"),
  path("create/",views.employee_create,name="employee_create"
),
   
]