# Generated by Django 5.1.4 on 2024-12-31 08:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0025_alter_emc_test_emc'),
    ]

    operations = [
        migrations.AddField(
            model_name='emc',
            name='Notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notlar'),
        ),
        migrations.CreateModel(
            name='EUT_Hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pump', models.CharField(blank=True, max_length=100, null=True, verbose_name='Pump')),
                ('Motor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Motor')),
                ('Fan', models.CharField(blank=True, max_length=100, null=True, verbose_name='Fan')),
                ('EMI_Filter', models.CharField(blank=True, max_length=100, null=True, verbose_name='EMI Filter')),
                ('Main_Board', models.CharField(blank=True, max_length=100, null=True, verbose_name='Main Board')),
                ('Display', models.CharField(blank=True, max_length=100, null=True, verbose_name='Display')),
                ('Driver_Board', models.CharField(blank=True, max_length=100, null=True, verbose_name='Driver Board')),
                ('Twinjet', models.CharField(blank=True, max_length=100, null=True, verbose_name='Twinjet')),
                ('Circulation_Pump', models.CharField(blank=True, max_length=100, null=True, verbose_name='Circulation Pump')),
                ('EMC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tasks.emc', verbose_name='EMC Testi')),
            ],
        ),
        migrations.CreateModel(
            name='EUT_Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Main_Board_Software', models.CharField(blank=True, max_length=100, null=True, verbose_name='Main Board Software')),
                ('Display_Software', models.CharField(blank=True, max_length=100, null=True, verbose_name='Display Software')),
                ('Driver_Board_Software', models.CharField(blank=True, max_length=100, null=True, verbose_name='Driver Board Software')),
                ('MPF', models.CharField(blank=True, max_length=100, null=True, verbose_name='MPF')),
                ('EMC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tasks.emc', verbose_name='EMC Testi')),
            ],
        ),
    ]
