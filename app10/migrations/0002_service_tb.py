# Generated by Django 4.1.7 on 2023-02-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app10', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='service_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=225)),
                ('description', models.TextField()),
            ],
        ),
    ]
