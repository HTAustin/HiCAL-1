# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-07-27 00:04
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Judgement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_id', models.CharField(max_length=512)),
                ('doc_title', models.TextField()),
                ('doc_CAL_snippet', models.TextField()),
                ('doc_search_snippet', models.TextField()),
                ('query', models.TextField(blank=True, null=True)),
                ('highlyRelevant', models.NullBooleanField()),
                ('nonrelevant', models.NullBooleanField()),
                ('relevant', models.NullBooleanField()),
                ('fromMouse', models.NullBooleanField()),
                ('fromKeyboard', models.NullBooleanField()),
                ('isFromCAL', models.NullBooleanField()),
                ('isFromSearch', models.NullBooleanField()),
                ('isFromSearchModal', models.NullBooleanField()),
                ('isFromIterative', models.NullBooleanField()),
                ('search_query', models.TextField(blank=True, null=True)),
                ('ctrl_f_terms_input', models.TextField(blank=True, null=True)),
                ('found_ctrl_f_terms_in_title', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, null=True)),
                ('found_ctrl_f_terms_in_summary', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, null=True)),
                ('found_ctrl_f_terms_in_full_doc', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, null=True)),
                ('timeVerbose', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, null=True, verbose_name='History')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
