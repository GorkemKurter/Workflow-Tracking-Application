# Generated by Django 5.1a1 on 2024-12-03 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0015_alter_task_task_asigned_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='Subtask_status',
            field=models.CharField(choices=[('NotResolved', 'Tamamlanmadı'), ('Ongoing', 'Devam Ediyor'), ('Finished', 'Tamamlandı'), ('Pending', 'Beklemede'), ('Cancelled', 'İptal Edildi')], default='NotResolved', max_length=20, verbose_name='Durum'),
        ),
    ]
