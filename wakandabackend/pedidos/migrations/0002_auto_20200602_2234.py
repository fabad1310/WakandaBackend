# Generated by Django 3.0.6 on 2020-06-02 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallepedido',
            name='precio',
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
