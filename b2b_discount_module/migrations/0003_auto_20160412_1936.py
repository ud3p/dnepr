# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('b2b_discount_module', '0002_auto_20160412_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_iso', models.CharField(max_length=255)),
                ('country_name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.OneToOneField(null=True, blank=True, to='b2b_discount_module.Country'),
        ),
    ]
