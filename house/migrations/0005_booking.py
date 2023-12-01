# Generated by Django 4.2.5 on 2023-10-09 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0004_remove_estate_housename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date_arrived', models.DateField(auto_now_add=True)),
                ('time_arrived', models.TimeField(auto_now_add=True)),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.estate')),
            ],
        ),
    ]