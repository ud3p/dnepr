# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('b2b_discount_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_iso',
            field=models.CharField(help_text=b'This field fill automatically!', max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='country_name',
            field=models.CharField(help_text=b'This field fill automatically!', max_length=255, null=True, blank=True),
        ),
    ]
