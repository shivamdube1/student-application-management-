from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ApplicationForm
from .models import Application

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Invalid credentials"
    return render(request, 'login.html', {'error': error})

@login_required
def dashboard_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('dashboard')
    else:
        form = ApplicationForm()
    applications = Application.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'form': form, 'applications': applications})

@login_required
def status_view(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'status.html', {'applications': applications})

@login_required
def admin_panel_view(request):
    if not request.user.is_superuser:
        return redirect('dashboard')
    if request.method == 'POST':
        app_id = request.POST.get('app_id')
        status = request.POST.get('status')
        Application.objects.filter(id=app_id).update(status=status)
    applications = Application.objects.all()
    return render(request, 'admin_panel.html', {'applications': applications})
