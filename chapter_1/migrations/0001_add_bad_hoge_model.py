# Generated by Django 5.0.2 on 2024-02-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BadHoge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_falg', models.IntegerField(default=0, null=True, verbose_name='削除フラグ')),
            ],
            options={
                'db_table': 'bad_hoge',
            },
        ),
    ]