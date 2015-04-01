# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150401_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myself',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aboutme', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
