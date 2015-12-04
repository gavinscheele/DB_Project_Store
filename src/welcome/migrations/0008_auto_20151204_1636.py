# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0007_remove_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contain',
            name='customerOrder',
            field=models.ForeignKey(to='welcome.customerOrder', default='1'),
        ),
    ]
