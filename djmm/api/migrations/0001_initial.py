# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 22:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Backtest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.SmallIntegerField(blank=True, null=True)),
                ('godprofit', models.SmallIntegerField(blank=True, null=True)),
                ('setprofit', models.SmallIntegerField(blank=True, null=True)),
                ('startcash', models.DecimalField(decimal_places=2, max_digits=10)),
                ('godresult', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('startdate', models.DateField()),
                ('duration', models.SmallIntegerField()),
                ('startquote', models.DecimalField(decimal_places=2, max_digits=10)),
                ('position', models.SmallIntegerField()),
                ('broker', models.CharField(max_length=10)),
                ('select_r', models.CharField(max_length=3)),
                ('symbols', models.TextField(blank=True, default='')),
                ('diversify', models.CharField(max_length=3)),
                ('hold', models.CharField(max_length=3)),
                ('margin', models.CharField(max_length=3)),
                ('swing', models.CharField(max_length=3)),
                ('positions', models.SmallIntegerField()),
                ('quantity', models.SmallIntegerField()),
                ('sharebuffer', models.SmallIntegerField()),
                ('transactions', models.SmallIntegerField(blank=True, null=True)),
                ('profitlimitpercent', models.SmallIntegerField()),
                ('stoplosspercentage', models.SmallIntegerField()),
                ('buystop_percentage', models.SmallIntegerField()),
                ('sellstoppercentage', models.SmallIntegerField()),
                ('trailingpercentage', models.SmallIntegerField()),
                ('buffer_test', models.SmallIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_assigned', models.DateTimeField(blank=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='backtest', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
