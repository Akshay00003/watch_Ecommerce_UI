# Generated by Django 4.2.4 on 2023-08-15 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('Quandity', models.CharField(max_length=10)),
                ('Order_Date', models.DateField(auto_now=True)),
            ],
        ),
    ]
