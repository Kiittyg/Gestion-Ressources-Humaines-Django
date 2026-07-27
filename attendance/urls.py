from django.urls import path
from . import views

urlpatterns = [
    path("check-in/", views.check_in, name="check_in"),
    path("check-out/", views.check_out, name="check_out"),
    path("list/", views.attendance_list, name="attendance_list"),
    path( "generate-absences/", views.generate_absences,name="generate_absences"),
                 
                  
                 

]