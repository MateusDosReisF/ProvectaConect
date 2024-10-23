# Generated by Django 5.0.1 on 2024-10-14 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContaPagar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_vencimento', models.DateField()),
                ('pago', models.BooleanField(default=False)),
                ('data_pagamento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContaReceber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_vencimento', models.DateField()),
                ('recebido', models.BooleanField(default=False)),
                ('data_recebimento', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
