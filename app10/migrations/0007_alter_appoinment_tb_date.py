# Generated by Django 4.1.7 on 2023-03-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app10', '0006_appoinment_tb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinment_tb',
            name='date',
            field=models.CharField(max_length=225),
        ),
    ]
