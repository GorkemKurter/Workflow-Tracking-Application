# Generated by Django 5.1a1 on 2024-11-18 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LVD_Management_System', '0022_alter_component_certificate_expiry_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='SAP_code',
            field=models.CharField(max_length=80, verbose_name='SAP Code'),
        ),
        migrations.AlterField(
            model_name='component_request',
            name='R_SAP_code',
            field=models.CharField(max_length=80, verbose_name='SAP Code'),
        ),
    ]
