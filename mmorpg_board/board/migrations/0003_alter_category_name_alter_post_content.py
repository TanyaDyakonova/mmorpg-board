# Generated by Django 5.2.3 on 2025-06-18 20:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_post_options_alter_reply_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('tank', 'Танки'), ('healer', 'Хилы'), ('dd', 'ДД'), ('merchant', 'Торговцы'), ('guildmaster', 'Гилдмастеры'), ('questgiver', 'Квестгиверы'), ('blacksmith', 'Кузнецы'), ('leatherworker', 'Кожевники'), ('alchemist', 'Зельевары'), ('spellmaster', 'Мастера заклинаний')], max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
