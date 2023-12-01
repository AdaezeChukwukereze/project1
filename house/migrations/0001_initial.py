# Generated by Django 4.2.5 on 2023-10-03 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatename', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=20)),
                ('slug', models.SlugField()),
                ('description', models.CharField(max_length=20)),
                ('bedrooms', models.IntegerField()),
                ('bathroom', models.IntegerField()),
                ('square_feet', models.IntegerField()),
                ('year_built', models.IntegerField()),
                ('price', models.IntegerField()),
                ('features', models.CharField(max_length=25)),
                ('main_photo', models.ImageField(upload_to='image')),
                ('additional_photos', models.ImageField(upload_to='images')),
            ],
        ),
    ]