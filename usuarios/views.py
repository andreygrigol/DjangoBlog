from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Registro

def register(request):
    if request.method == 'POST':
        form = Registro(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso, {username}!')
            return redirect('blog-home')
    else:
        form = Registro()
    return render(request, 'usuarios/register.html', {'form': form})
