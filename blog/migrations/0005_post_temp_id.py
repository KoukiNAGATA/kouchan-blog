# Generated by Django 3.2.4 on 2021-08-22 09:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='temp_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
