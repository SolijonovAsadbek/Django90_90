from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(to='/login/')
    else:
        form = AuthenticationForm(request=request)
    context = {
        'auth_form': form
    }
    return render(request=request, template_name='accounts/login.html', context=context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect(to='/login/')
    return render(request=request, template_name='accounts/logout.html')


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(to='/login')
    context = {
        'register_form': form
    }
    return render(request=request, template_name='accounts/register.html', context=context)
