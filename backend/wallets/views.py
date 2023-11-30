from django.shortcuts import render
import requests
from rest_framework.views import APIView
from django.http import JsonResponse
from wallets.models import Wallet
from wallets.serializers import WalletSerializer
from rest_framework.response import Response
from decimal import Decimal

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

class BuyView(APIView):
    def post(self, request, qty):
        qty = Decimal(str(qty))
        # qty = float(qty) # Pasamos <str:qty> a float
        price_response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=clp")
        price = price_response.json()["bitcoin"]["clp"]
        user_wallet = request.user.wallet
        if user_wallet.balance_clp >= qty*price: # Tiene suficiente plata para comprar?
            user_wallet.balance_btc += qty # compra qty BTC
            user_wallet.balance_clp -= qty*price # a cambio pierde qty*price CLP
            user_wallet.save() # guardamos
            serializer = WalletSerializer(user_wallet)
            return Response(serializer.data)
        else:
            return Response(status=400) # Bad Request: no tiene suficiente plata

class SellView(APIView):
    def post(self, request, qty):
        print("la cantidad es :" ,qty)
        qty = Decimal(str(qty))
        # qty = float(qty) # Pasamos <str:qty> a float
        price_response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=clp")
        price = price_response.json()["bitcoin"]["clp"]
        user_wallet = request.user.wallet

        if user_wallet.balance_btc > 0: # Tiene suficientes bitcoins para vender?
            user_wallet.balance_clp += qty*price # gana CLP qty*price
            user_wallet.balance_btc -= qty # vende qty BTC
            user_wallet.save() # guardamos
            serializer = WalletSerializer(user_wallet)
            return Response(serializer.data)
        else:
            return Response(status=400) # Bad Request: no tiene suficiente plata