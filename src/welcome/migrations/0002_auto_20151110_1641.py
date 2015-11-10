# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contains',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(to='welcome.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('active', models.BooleanField()),
                ('description', models.CharField(max_length=100)),
                ('stockQuantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('name', models.CharField(max_length=100)),
                ('orders', models.ManyToManyField(to='welcome.Order', through='welcome.Contains')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(to='welcome.Supplier'),
        ),
        migrations.AddField(
            model_name='contains',
            name='product',
            field=models.ForeignKey(to='welcome.Product'),
        ),
    ]
