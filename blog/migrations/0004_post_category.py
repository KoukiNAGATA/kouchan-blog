# Generated by Django 3.2.4 on 2021-06-05 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='カテゴリー'),
            preserve_default=False,
        ),
    ]
