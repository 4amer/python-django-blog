# Generated by Django 4.1.3 on 2022-11-27 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_article_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_text',
        ),
    ]