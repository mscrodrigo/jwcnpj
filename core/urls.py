from django.urls import path  # v2 estamos importando do django.urls

from .views import index, contato, produto  # v2 importando as views index e contato

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
    # criando uma rota para produto enviando o id , view produto, nome da rota é produto
]
