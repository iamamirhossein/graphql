# Generated by Django 4.0.3 on 2022-06-04 13:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('decks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('bucket', models.IntegerField(choices=[(1, '1 Day'), (2, '3 Days'), (3, '7 Days'), (4, '16 Days'), (5, '30 Days')], default=1)),
                ('next_review_at', models.DateTimeField(default=datetime.datetime(2022, 6, 4, 13, 38, 49, 457438, tzinfo=utc))),
                ('last_reviewed_at', models.DateTimeField(blank=True, null=True)),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decks.deck')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
