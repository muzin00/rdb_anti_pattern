# Generated by Django 5.0.2 on 2024-03-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter_2', '0001_add_ec_site_tables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumptiontax',
            name='expiration_date',
            field=models.DateField(null=True, verbose_name='失効日'),
        ),
    ]
