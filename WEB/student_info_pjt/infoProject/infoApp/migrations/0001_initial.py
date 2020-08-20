# Generated by Django 3.1 on 2020-08-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AiClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('teacher', models.CharField(max_length=25)),
                ('room', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='AiStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('class_number', models.IntegerField()),
                ('introduce', models.TextField()),
                ('github', models.CharField(max_length=250)),
            ],
        ),
    ]
