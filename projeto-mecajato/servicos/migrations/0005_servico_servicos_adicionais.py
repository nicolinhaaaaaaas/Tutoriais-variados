# Generated by Django 5.0.1 on 2024-01-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0004_servicoadicional'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='servicos_adicionais',
            field=models.ManyToManyField(to='servicos.servicoadicional'),
        ),
    ]
