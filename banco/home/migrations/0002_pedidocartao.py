# Generated by Django 4.1.3 on 2022-11-29 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoCartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=11)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('senha', models.CharField(max_length=6)),
            ],
        ),
    ]
