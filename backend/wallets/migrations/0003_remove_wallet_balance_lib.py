# Generated by Django 3.2.21 on 2023-11-16 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0002_wallet_balance_lib'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='balance_lib',
        ),
    ]
