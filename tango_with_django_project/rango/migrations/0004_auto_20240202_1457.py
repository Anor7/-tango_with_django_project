# Generated by Django 2.2.28 on 2024-02-02 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_choice_question'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
