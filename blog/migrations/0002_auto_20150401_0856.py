# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-time']},
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
