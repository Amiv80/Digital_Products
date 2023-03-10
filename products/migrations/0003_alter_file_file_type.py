# Generated by Django 3.2 on 2023-02-28 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230228_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'audio'), (2, 'video'), (3, 'pdf')], default=1, verbose_name='file type'),
            preserve_default=False,
        ),
    ]
