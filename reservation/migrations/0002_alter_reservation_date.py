# Generated by Django 4.0.4 on 2022-09-21 07:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
