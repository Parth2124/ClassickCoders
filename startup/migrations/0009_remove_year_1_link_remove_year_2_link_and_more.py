# Generated by Django 5.0.6 on 2024-11-14 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0008_year_1_link_year_2_link_year_3_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='year_1',
            name='link',
        ),
        migrations.RemoveField(
            model_name='year_2',
            name='link',
        ),
        migrations.RemoveField(
            model_name='year_3',
            name='link',
        ),
    ]
