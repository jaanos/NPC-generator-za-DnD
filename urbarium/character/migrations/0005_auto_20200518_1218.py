# Generated by Django 3.0.4 on 2020-05-18 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0004_auto_20200518_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='notes',
            field=models.TextField(blank=True, default='', max_length=1000),
            preserve_default=False,
        ),
    ]