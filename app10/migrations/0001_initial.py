# Generated by Django 4.1.7 on 2023-02-23 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=225)),
                ('password', models.CharField(max_length=225)),
                ('confirmpassword', models.CharField(max_length=225)),
            ],
        ),
    ]
