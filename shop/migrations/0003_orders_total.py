# Generated by Django 3.2.4 on 2021-07-03 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='total',
            field=models.CharField(default='1', max_length=2000),
            preserve_default=False,
        ),
    ]