# Generated by Django 5.1a1 on 2024-12-20 05:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0017_iecee_tests'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topic', models.CharField(max_length=100, verbose_name='Konu')),
                ('Company', models.CharField(max_length=100, verbose_name='Firma')),
                ('Month', models.DateField(auto_now_add=True, verbose_name='Tarih')),
                ('Year', models.CharField(max_length=100, verbose_name='Yıl')),
                ('SAT', models.CharField(max_length=100, verbose_name='SAT No.')),
                ('SAS', models.CharField(max_length=100, verbose_name='SAS No.')),
                ('Amount', models.CharField(max_length=100, verbose_name='Tutar')),
                ('Currency', models.CharField(max_length=100, verbose_name='Para Birimi')),
                ('Status', models.CharField(max_length=100, verbose_name='Onay Durumu')),
                ('Comments', models.CharField(max_length=200, verbose_name='Açıklama')),
                ('Requester', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Talep Eden')),
            ],
        ),
    ]
