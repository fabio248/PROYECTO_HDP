# Generated by Django 3.2.4 on 2021-06-26 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_auto_20210626_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsidioagua',
            name='cantidad_subsidio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Cantidad subsidiada'),
        ),
    ]
