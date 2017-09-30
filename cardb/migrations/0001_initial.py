# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 01:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('name_cn', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Carmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('name_cn', models.CharField(max_length=40)),
                ('wheelbase', models.IntegerField(blank=True)),
                ('ftrack', models.IntegerField(blank=True)),
                ('rtrack', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('name_cn', models.CharField(max_length=100)),
                ('logo', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='carmodel',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardb.Manufacturer'),
        ),
        migrations.AddField(
            model_name='car',
            name='carmodel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardb.Carmodel'),
        ),
        migrations.AddField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardb.Manufacturer'),
        ),
    ]
