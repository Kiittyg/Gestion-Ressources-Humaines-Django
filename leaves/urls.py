from django.urls import path
from . import views

urlpatterns = [

    # demande de congé
    path(
        "request/",views.leave_request,name="leave_request"
    ),
    path( "list/", views.leave_list, name="leave_list"
),
    path("approve/<int:pk>/", views.approve_leave,name="approve_leave"
),

     path("reject/<int:pk>/", views.reject_leave, name="reject_leave"
),
     path("mes-conges/",views.employee_leave_list,name="employee_leave_list"
),
]