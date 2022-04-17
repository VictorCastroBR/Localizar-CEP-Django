from django.shortcuts import redirect, render
from django.contrib import messages
import requests

def index(request):
    
    if request.method == 'POST':
      
        get_cep = request.POST.get('cep')
        if len(get_cep) != 8: 
          messages.error(request, 'CEP inválido!')
        else:
          address = requests.get(f'https://viacep.com.br/ws/{get_cep}/json/')
          try:
            address = address.json()
          except:
            messages.error(request, 'CEP inválido!')
            return redirect ('/')
        
          if not 'erro' in address:
              context = {
                  'cep': address['cep'],
                  'logradouro': address['logradouro'],
                  'complemento': address['complemento'],
                  'localidade': address['localidade'],
                  'uf': address['uf'],
                  'ibge': address['ibge'],
                  'ddd': address['ddd'],
              }
          
          else:
              messages.error(request, 'CEP inválido!')
              return redirect ('/')

          return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')

    return redirect ('/')