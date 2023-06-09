# Generated by Django 4.2 on 2023-04-23 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_comment_last_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='updated_on',
            new_name='last_updated',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='last_updated',
        ),
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
