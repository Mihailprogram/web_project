# Generated by Django 2.2.16 on 2023-01-16 08:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0008_follow'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment1',
            new_name='Comment',
        ),
    ]
