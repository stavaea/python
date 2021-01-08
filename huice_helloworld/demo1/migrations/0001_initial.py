# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': '\u4f5c\u8005\u8868',
                'verbose_name_plural': '\u4f5c\u8005\u8868',
            },
        ),
        migrations.CreateModel(
            name='AuthorDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('sex', models.IntegerField(choices=[(0, b'\xe7\x94\xb7'), (1, b'\xe5\xa5\xb3')])),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=30)),
                ('author', models.OneToOneField(to='demo1.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('price', models.FloatField(max_length=20)),
                ('authors', models.ManyToManyField(to='demo1.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=18)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(to='demo1.Publisher'),
        ),
    ]
