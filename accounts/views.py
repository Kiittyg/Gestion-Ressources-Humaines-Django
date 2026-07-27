from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout




def login_view(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            if user.role == "RH":
                return redirect("dashboard_home")
            else:
                return redirect("employee_dashboard")

        else:
            return render(request, "accounts/login.html", {
                "error": "Email ou mot de passe incorrect"
            })

    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)

    # Retour à la page de connexion
    return redirect("login")

# def rh_dashboard(request):
#     return render(request, "accounts/rh_dashboard.html")




