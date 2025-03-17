from django.shortcuts import render
import requests
from django.http import HttpResponse

API_KEY = "a9631434f59e4a2893f104916251703"
URL_BASE = "http://api.weatherapi.com/v1/"

# Página inicial
def home(request):
    return render(request, 'home.html')

# Busca de clima e exibição de resultados
def buscar_clima(request):
    cidade = request.GET.get('cidade', 'Salvador')  # Cidade padrão é Salvador
    url = f"{URL_BASE}current.json?key={API_KEY}&q={cidade}&lang=pt"
    
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()
        contexto = {
            'cidade': dados['location']['name'],
            'temperatura': dados['current']['temp_c'],
            'descricao': dados['current']['condition']['text'],
            'vento': dados['current']['wind_kph'],
            'umidade': dados['current']['humidity'],
        }
        return render(request, 'resultados.html', contexto)
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Erro ao acessar a API: {e}", status=500)
