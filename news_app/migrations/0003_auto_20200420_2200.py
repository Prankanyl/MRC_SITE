# Generated by Django 3.0.5 on 2020-04-20 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_article_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='news_app/image/% Y/% m/% d/', verbose_name='Фотография'),
        ),
    ]
