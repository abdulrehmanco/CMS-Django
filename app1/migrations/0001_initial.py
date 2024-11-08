# Generated by Django 3.2.5 on 2022-05-08 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contact', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('desc', models.TextField(max_length=500, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('contact', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('salary', models.IntegerField()),
                ('joining_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('sell_price', models.CharField(max_length=200, null=True)),
                ('buy_price', models.CharField(max_length=200, null=True)),
                ('desc', models.CharField(max_length=200, null=True)),
                ('in_stock', models.CharField(max_length=200, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('shelf_no', models.CharField(max_length=50, null=True)),
                ('company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.medicine')),
            ],
        ),
    ]
