from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Registro

def register(request):
    if request.method == 'POST':
        form = Registro(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso, {username}!')
            return redirect('login')
    else:
        form = Registro()
    return render(request, 'usuarios/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'usuarios/profile.html')
