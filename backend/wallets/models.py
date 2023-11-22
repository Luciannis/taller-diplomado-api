# wallets/models.py
from accounts.models import User
# from django.contrib.auth.models import User
from django.db import models

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance_btc = models.DecimalField(max_digits=15, decimal_places=8, default=0)
    balance_clp = models.DecimalField(max_digits=15, decimal_places=2, default=0)
