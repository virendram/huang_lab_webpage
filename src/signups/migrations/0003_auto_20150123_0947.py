# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0002_signup_universityname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='universityname',
            new_name='Organization',
        ),
    ]
