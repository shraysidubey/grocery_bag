# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gro_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=100)),
                ('quantity', models.FloatField()),
                ('flag', models.CharField(max_length=11, choices=[(b'bought', b'bought'), (b'left', b'left'), (b'available', b'available')])),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('user_profile', models.ForeignKey(to='gro_app.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
