# Generated by Django 3.2.5 on 2022-05-11 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_company_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='user',
        ),
    ]