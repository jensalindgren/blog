# Generated by Django 4.2 on 2023-04-23 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'comments'},
        ),
    ]
