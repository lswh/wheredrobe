# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothingplain',
            name='itemstatus',
            field=models.CharField(choices=[('CB', 'In the Cabinet'), ('RS', 'Under Alterations'), ('H', 'In the Hamper'), ('LS', 'At the Laundry Shop'), ('M', 'Missing')], max_length=2, default='CB'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clothingplain',
            name='picture',
            field=models.ImageField(upload_to='', default=None),
            preserve_default=True,
        ),
    ]
