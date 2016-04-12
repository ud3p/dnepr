# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('b2b_discount_module', '0003_auto_20160412_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_iso',
            field=models.CharField(max_length=3, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
