# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150401_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
