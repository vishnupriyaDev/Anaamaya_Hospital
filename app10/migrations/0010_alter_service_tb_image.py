# Generated by Django 4.1.7 on 2023-03-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app10', '0009_service_tb_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_tb',
            name='image',
            field=models.ImageField(upload_to='service/'),
        ),
    ]
