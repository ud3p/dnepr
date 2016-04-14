# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('b2b_discount_module', '0004_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='period',
            name='choose_period',
            field=models.ForeignKey(default=1, to='b2b_discount_module.Agreement'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='period',
            name='period_end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='period',
            name='period_start_date',
            field=models.DateField(),
        ),
    ]
