# Generated by Django 5.0.1 on 2024-01-26 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scrapper', '0002_countriesonline_alter_proxy_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='countriesonline',
            name='last_update',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
