# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('street_numer', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=200)),
                ('post_numer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.URLField()),
                ('logo', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(related_name='companies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_start_date', models.DateTimeField(null=True)),
                ('rent_end_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('total_desks', models.IntegerField(verbose_name='Total desks')),
                ('reserved_desks', models.IntegerField(verbose_name='Reserved desks')),
                ('price', models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Price per desk $')),
                ('address', models.ForeignKey(to='cowork.Address')),
                ('company', models.ForeignKey(related_name='locations', to='cowork.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Vat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('vat', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='desk',
            name='location',
            field=models.OneToOneField(to='cowork.Location', related_name='desks'),
        ),
        migrations.AddField(
            model_name='desk',
            name='owner',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, related_name='desks'),
        ),
        migrations.AddField(
            model_name='company',
            name='vat_id',
            field=models.ForeignKey(to='cowork.Vat'),
        ),
    ]
