# Generated by Django 5.0.6 on 2024-06-26 05:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=250)),
                ('explanation', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.CharField(default='Korea', max_length=50)),
                ('city', models.CharField(default='Seoul', max_length=80)),
                ('name', models.CharField(max_length=250)),
                ('price', models.PositiveBigIntegerField()),
                ('address', models.CharField(max_length=250)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('descriptions', models.TextField()),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('perks', models.ManyToManyField(to='experiences.perk')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
