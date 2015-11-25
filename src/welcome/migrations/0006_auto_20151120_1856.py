# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0005_auto_20151120_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerorder',
            old_name='date',
            new_name='createDate',
        ),
    ]
