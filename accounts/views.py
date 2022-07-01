from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request=request, template_name='accounts/login.html')

def logout_view(request):
    return render(request=request, template_name='accounts/logout.html')

def register_view(request):
    return render(request=request, template_name='accounts/register.html')