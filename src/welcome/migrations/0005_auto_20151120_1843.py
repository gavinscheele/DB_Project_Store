# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0004_product_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField()),
                ('user', models.ForeignKey(to='welcome.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='contain',
            name='order',
        ),
        migrations.RemoveField(
            model_name='product',
            name='orders',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AddField(
            model_name='contain',
            name='customerOrder',
            field=models.ForeignKey(default=b'1', to='welcome.customerOrder'),
        ),
        migrations.AddField(
            model_name='product',
            name='customerOrders',
            field=models.ManyToManyField(to='welcome.customerOrder', through='welcome.Contain'),
        ),
    ]
