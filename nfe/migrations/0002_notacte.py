# Generated by Django 5.0.1 on 2024-10-20 01:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotaCTe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20)),
                ('nf', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=100)),
                ('status_CTE', models.CharField(max_length=100)),
                ('emissor', models.CharField(max_length=100)),
                ('emissor_cnpj', models.CharField(max_length=20)),
                ('destinatario', models.CharField(max_length=100)),
                ('destinatario_cnpj', models.CharField(max_length=20)),
                ('valor_total', models.CharField(max_length=20)),
                ('xml', models.TextField()),
                ('chaveCTe', models.CharField(max_length=100)),
                ('etiqueta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='etiqueta_CTE', to='nfe.etiqueta')),
            ],
        ),
    ]
