from django.shortcuts import render

posts = [
    {
        'autor': 'Marcelo',
        'titulo': 'Primeiro post',
        'conteudo': 'Conteudo do primeiro post',
        'data': '20 de Julho, 2023'
    },
    {
        'autor': 'Gustavo',
        'titulo': 'Segundo post',
        'conteudo': 'Conteudo do segundo post',
        'data': '21 de Julho, 2023'
    }
]

def home(request):
    contexto = {
        'posts': posts

    }
    return render(request, 'blog/home.html', contexto)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

