# Generated by Django 5.1a1 on 2024-11-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LVD_Management_System', '0002_rename_components_component'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='F_Washer_Dryer_LVD',
            field=models.BooleanField(default=True, verbose_name='T washer'),
        ),
        migrations.AddField(
            model_name='component',
            name='F_Washer_LVD',
            field=models.BooleanField(default=True, verbose_name='T washer'),
        ),
        migrations.AddField(
            model_name='component',
            name='N_Washer_LVD',
            field=models.BooleanField(default=True, verbose_name='T washer'),
        ),
        migrations.AddField(
            model_name='component',
            name='T_Washer_Dryer_LVD',
            field=models.BooleanField(default=True, verbose_name='T washer'),
        ),
        migrations.AddField(
            model_name='component',
            name='T_Washer_LVD',
            field=models.BooleanField(default=True, verbose_name='T washer'),
        ),
        migrations.AlterField(
            model_name='component',
            name='Part_name',
            field=models.CharField(choices=[('Main Motor - UM', 'Main Motor - UM'), ('Main motor - BLDC', 'Main motor - BLDC'), ('Drain pump (for twin jet system)', 'Drain pump (for twin jet system)'), ('Drain pump', 'Drain pump'), ('Circulation pump (for twin jet system)', 'Circulation pump (for twin jet system)'), ('Drain pump (twin jet system) (with emergency exit hose)', 'Drain pump (twin jet system) (with emergency exit hose)'), ('Dosage pump', 'Dosage pump'), ('Hydroboost pump', 'Hydroboost pump'), ('Capacitor (for Hydro-boost pump)', 'Capacitor (for Hydro-boost pump)'), ('Thermal Protector', 'Thermal Protector'), ('Belt (BLDC models)', 'Belt (BLDC models)'), ('Electrically operated door lock', 'Electrically operated door lock'), ('Door switch with interlock', 'Door switch with interlock'), ('Heating element', 'Heating element'), ('with 2 fuse', 'with 2 fuse'), ('with alternative 2 fuse', 'with alternative 2 fuse'), ('Heating element (Pyrojet)', 'Heating element (Pyrojet)'), ('Inlet valve (double)', 'Inlet valve (double)'), ('Inlet valve (single)', 'Inlet valve (single)'), ('Inlet valve (triple)', 'Inlet valve (triple)'), ('Level switch', 'Level switch'), ('Level sensor', 'Level sensor'), ('NTC', 'NTC'), ('Reed Switch', 'Reed Switch'), ('Steam Generator', 'Steam Generator'), ('with Thermostat', 'with Thermostat'), ('Thermostat for Pyrojet Heating Element', 'Thermostat for Pyrojet Heating Element'), ('Overflow Switch', 'Overflow Switch'), ('Electronic Module - BLDC Board', 'Electronic Module - BLDC Board'), ('Electronic Module - DC Board', 'Electronic Module - DC Board'), ('Electronic Module - Steamjet, Pyrojet, Dryer Board', 'Electronic Module - Steamjet, Pyrojet, Dryer Board'), ('Electronic Module - IO Board', 'Electronic Module - IO Board'), ('Electronic Module - Door Light Board', 'Electronic Module - Door Light Board'), ('Electronic Module - Main Board', 'Electronic Module - Main Board'), ('Electronic Module - UI Board', 'Electronic Module - UI Board'), ('Drum Light Board', 'Drum Light Board'), ('Electronic Module - Sterilizone IO Board', 'Electronic Module - Sterilizone IO Board'), ('Electronic Module - Intelliwash IO Board', 'Electronic Module - Intelliwash IO Board'), ('Electronic Module - LED Board', 'Electronic Module - LED Board'), ('Electronic Module - UV Ballast Board', 'Electronic Module - UV Ballast Board'), ('Electronic Module - UV Lamp Board', 'Electronic Module - UV Lamp Board'), ('Electronic Module - Wifi Board', 'Electronic Module - Wifi Board'), ('EMI filter', 'EMI filter'), ('Current Fuse', 'Current Fuse'), ('Microcontroller - BLDC Board', 'Microcontroller - BLDC Board'), ('Microcontroller - Main Board', 'Microcontroller - Main Board'), ('Optocoupler', 'Optocoupler'), ('Optotriac', 'Optotriac'), ('Relay on PCB', 'Relay on PCB'), ('Safety Transformer', 'Safety Transformer'), ('Switch on PCB', 'Switch on PCB'), ('Varistor', 'Varistor'), ('XY Capacitor', 'XY Capacitor'), ('Plug Current Fuse', 'Plug Current Fuse'), ('hose set (cold)', 'hose set (cold)'), ('hose set (hot)', 'hose set (hot)'), ('Check Valve', 'Check Valve'), ('Supply cord', 'Supply cord'), ('Plug', 'Plug')], max_length=100, verbose_name='Object / part No.'),
        ),
        migrations.AlterField(
            model_name='component',
            name='Standard',
            field=models.TextField(verbose_name='Standard(s)'),
        ),
    ]
