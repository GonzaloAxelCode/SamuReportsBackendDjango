# Generated by Django 3.1.7 on 2023-07-14 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploadcsv', '0003_alter_data_cnv_cnv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maestro_his_paciente',
            name='CNV',
        ),
    ]
