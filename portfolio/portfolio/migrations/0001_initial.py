# Generated by Django 4.0.1 on 2023-05-31 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=500)),
                ('bg', models.CharField(max_length=500)),
                ('fb', models.CharField(max_length=500)),
            ],
        ),
    ]