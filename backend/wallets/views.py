from django.shortcuts import render
import requests
from rest_framework.views import APIView
from django.http import JsonResponse

# Create your views here.
class ChartView(APIView):
    def get(self,request):
        url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
        params = {
            'vs_currency': 'clp',
            'days': '90'
        }
        response = requests.get(url,params)

        if(response.status_code == 200):
            data = response.json()
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'No se pudieron obtener los datos'})

class PriceView(APIView):
    def get(self,request):
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=clp'
        params = {
            'ids':'bitcoin',
            'vs_currencies':'clp'
        }
        response = requests.get(url,params)

        if(response.status_code == 200):
            data = response.json()
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'No se pudieron obtener los datos'})