# Generated by Django 5.1a1 on 2024-11-13 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LVD_Management_System', '0005_component_sap_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='SAP_code',
            field=models.IntegerField(default='0', max_length=80, verbose_name='SAP Code'),
        ),
    ]
