# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20150401_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothingplain',
            name='clothing_type',
            field=models.CharField(max_length=2, choices=[('T', 'Shirts or Tops or Polos'), ('B', 'Skirts or Shorts or Pants'), ('FW', 'Footwear'), ('D', 'Dresses or Onesies'), ('MI', 'Miscellaneous')], default='T'),
            preserve_default=True,
        ),
    ]
