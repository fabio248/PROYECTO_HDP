# Generated by Django 3.2.4 on 2021-06-26 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('apps', '0011_auto_20210626_2032'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Administrador',
        ),
    ]