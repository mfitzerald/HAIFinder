# Generated by Django 2.0.5 on 2018-05-27 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haipumpfinder', '0016_auto_20180527_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='ned',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='YES', max_length=20),
        ),
    ]