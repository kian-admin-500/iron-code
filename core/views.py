from django.shortcuts import render
from .forms import LoginForm
from .models import AdminTable

# Create your views here.

def Login_shower(request):
    form = LoginForm()
    all_account = AdminTable.objects.all

    if request.method == 'POST':
        form = LoginForm( request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'login.html', {
        'form': form,
        'all': all_account,
    })