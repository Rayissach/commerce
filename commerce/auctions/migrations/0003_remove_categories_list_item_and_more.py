# Generated by Django 4.2 on 2023-07-19 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_comments_listing_categories_bids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='list_item',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='description',
        ),
    ]