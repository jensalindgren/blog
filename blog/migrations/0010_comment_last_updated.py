# Generated by Django 4.2 on 2023-04-23 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
