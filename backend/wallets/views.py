from django.shortcuts import render
import requests
from rest_framework.views import APIView
from django.http import JsonResponse
from wallets.models import Wallet
from wallets.serializers import WalletSerializer
from rest_framework.response import Response

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

class WalletView(APIView):
    queryset = Wallet.objects
    serializer_class = WalletSerializer
    def get(self, request):
        current_user = request.user
        wallet_instance = Wallet.objects.get(user=current_user)
        serializer = WalletSerializer(wallet_instance)
        print(serializer)
        return Response(serializer.data)