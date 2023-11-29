# from django.contrib.auth import get_user_model
from wallets.models import Wallet
from rest_framework import serializers
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('balance_btc', 'balance_clp')