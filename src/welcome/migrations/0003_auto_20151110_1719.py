# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0002_auto_20151110_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contain',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(to='welcome.Order')),
            ],
        ),
        migrations.RemoveField(
            model_name='contains',
            name='order',
        ),
        migrations.RemoveField(
            model_name='contains',
            name='product',
        ),
        migrations.AlterField(
            model_name='product',
            name='orders',
            field=models.ManyToManyField(to='welcome.Order', through='welcome.Contain'),
        ),
        migrations.DeleteModel(
            name='Contains',
        ),
        migrations.AddField(
            model_name='contain',
            name='product',
            field=models.ForeignKey(to='welcome.Product'),
        ),
    ]
