# Generated by Django 4.0.6 on 2023-06-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyportal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
