# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='universityname',
            field=models.CharField(max_length=120, null=True),
            preserve_default=True,
        ),
    ]
