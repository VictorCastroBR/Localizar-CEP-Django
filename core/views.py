import re
from django.shortcuts import redirect, render
import requests


def index(request):
    if request.method == 'POST':
        get_cep = request.POST.get('cep')
        address = requests.get(f'https://viacep.com.br/ws/{get_cep}/json/')
        address = address.json()

        context = {
            'cep': address['cep'],
            'logradouro': address['logradouro'],
            'complemento': address['complemento'],
            'localidade': address['localidade'],
            'uf': address['uf'],
            'ibge': address['ibge'],
            'ddd': address['ddd'],
        }

        return render(request, 'index.html', context)

    else:
        return render(request, 'index.html')