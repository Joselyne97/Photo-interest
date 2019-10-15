# Generated by Django 2.2.6 on 2019-10-14 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]


    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pictures/')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=150)),
                ('category', models.ForeignKey(db_column='category', on_delete=django.db.models.deletion.CASCADE, to='photo.Category')),
                ('location', models.ForeignKey(db_column='location', on_delete=django.db.models.deletion.CASCADE, to='photo.Location')),
            ],
        ),
    ]
