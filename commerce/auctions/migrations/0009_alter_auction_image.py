# Generated by Django 4.0.2 on 2022-05-02 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_auction_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.ImageField(blank=True, default='placeholder.jpg', upload_to='images', verbose_name='lot image'),
        ),
    ]
