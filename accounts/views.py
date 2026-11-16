from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileUpdateForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard_router(request):
    if request.user.role == 'admin':
        return redirect('admin_dashboard')
    return redirect('customer_dashboard')

@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return redirect('dashboard_router') # Block unauthorized role access
    return render(request, 'accounts/admin_dashboard.html')

@login_required
def customer_dashboard(request):
    if request.user.role != 'customer':
        return redirect('dashboard_router') # Block unauthorized role access
    return render(request, 'accounts/customer_dashboard.html')

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileUpdateForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})