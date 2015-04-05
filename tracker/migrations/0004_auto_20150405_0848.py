# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_clothingplain_clothing_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothingplain',
            name='itemstatus',
            field=models.CharField(max_length=2, choices=[('CB', 'In the Cabinet'), ('RS', 'Under Alterations'), ('H', 'In the Hamper'), ('LS', 'At the Laundry Shop'), ('D', 'For Donation or Charity'), ('M', 'Missing')], default='CB'),
            preserve_default=True,
        ),
    ]
