# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('message_title', models.CharField(max_length=200)),
                ('author_name', models.CharField(max_length=200)),
                ('e_mail', models.EmailField(max_length=254)),
                ('message_text', models.TextField()),
                ('created_date_message', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'message',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('image_descriotion', models.ImageField(upload_to='')),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'project',
            },
        ),
    ]
