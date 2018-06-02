# Generated by Django 2.0.5 on 2018-05-27 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haipumpfinder', '0003_auto_20180527_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='msi_status',
            field=models.CharField(choices=[('MSS', 'MSS'), ('MSIH', 'MSI-H')], default='MSS', max_length=2),
        ),
    ]