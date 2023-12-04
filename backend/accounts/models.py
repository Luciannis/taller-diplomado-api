# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from wallets.models import Wallet

class User(AbstractUser):
    phone = models.CharField(max_length=13)

    def save(self, *args, **kwargs):
        is_new_user = not self.pk  # Verifica si el usuario es nuevo

        super().save(*args, **kwargs)  # Guarda el usuario

        if is_new_user:  # Si es un usuario nuevo
            initial_balance_clp = 50000  # $50,000 de bono de bienvenida
            Wallet.objects.create(user=self, balance_clp=initial_balance_clp)