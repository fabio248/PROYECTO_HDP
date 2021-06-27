# Generated by Django 3.2.4 on 2021-06-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_auto_20210626_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsidiogaslicuado',
            name='aprobado',
            field=models.BooleanField(default=False, help_text='Seleccione si la información brindada es correcta', verbose_name='Aprobación'),
        ),
        migrations.AddField(
            model_name='subsidiogaslicuado',
            name='verificado',
            field=models.BooleanField(default=False, help_text='Seleccione si ya reviso la información del usuario', verbose_name='Verificado'),
        ),
        migrations.AddField(
            model_name='subsidioluz',
            name='aprobado',
            field=models.BooleanField(default=False, help_text='Seleccione si la información brindada es correcta', verbose_name='Aprobación'),
        ),
        migrations.AddField(
            model_name='subsidioluz',
            name='verificado',
            field=models.BooleanField(default=False, help_text='Seleccione si ya reviso la información del usuario', verbose_name='Verificado'),
        ),
        migrations.AlterField(
            model_name='subsidioagua',
            name='aprobado',
            field=models.BooleanField(default=False, help_text='Seleccione si la información brindada es correcta', verbose_name='Aprobación'),
        ),
        migrations.AlterField(
            model_name='subsidioagua',
            name='verificado',
            field=models.BooleanField(default=False, help_text='Seleccione si ya reviso la información del usuario', verbose_name='Verificado'),
        ),
    ]