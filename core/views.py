# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import PatientLoginForm


# -------------------------
# PATIENT REGISTRATION
# -------------------------
def patient_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "patient"   # assign patient role
            user.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "core/patient_register.html", {"form": form})


# -------------------------
# PATIENT LOGIN
# -------------------------
def patient_login(request):
    if request.method == "POST":
        form = PatientLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = PatientLoginForm()
    return render(request, "core/patient_login.html", {"form": form})


# -------------------------
# PATIENT LOGOUT
# -------------------------
@login_required
def patient_logout(request):
    logout(request)
    return redirect("patient_login")


# -------------------------
# HOME / DASHBOARD
# -------------------------
@login_required
def home(request):
    return render(request, "core/home.html")
