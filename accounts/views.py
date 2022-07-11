from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # POST action uchun
        user = form.get_user()
        login(request, user)
        return redirect(to='/login/')
    else:
        form = AuthenticationForm(request)  # Bo`sh maydon uchun

    context = {
        'form': form
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
