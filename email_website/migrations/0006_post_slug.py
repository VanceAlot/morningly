# Generated by Django 3.1.3 on 2021-01-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_website', '0005_article_market_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
