from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Produto  # importa do models


def index(request):
    myprodutos = Produto.objects.all()  # aqui trará todos os produtos do banco de dados de Produtos

    # print(dir(request))
    # print(f"User': {request.user}")
    #
    # # print(f"User-Agent': {request.headers['User-Agent']}")
    # # print(f"User': {request.user}")
    # # print(f"sobrenome': {request.user.last_name}")
    # # print(f"email': {request.user.email}")
    #
    # if str(request.user) == 'AnonymousUser':
    #     teste = 'usuario não logado'
    # else:
    #     teste = 'usuario logado'
    # 'logado': teste  # para mostrar no if str(request.user)

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'É nois',
        'produtosview': myprodutos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    # print(f'PK: {pk}')
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)  # caso ele nao encontre redireciona para a pg 404
    context = {
        'produtov': prod
    }
    return render(request, 'produto.html', context)


# def error404(request, exception):
#     return render(request, '404.html')
#
def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)
    # return render(request, '404.html')


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)

