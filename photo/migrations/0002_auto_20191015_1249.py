# Generated by Django 2.2.6 on 2019-10-15 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='description',
            field=models.TextField(),
        ),
    ]
