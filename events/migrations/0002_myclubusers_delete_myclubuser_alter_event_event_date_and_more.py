# Generated by Django 5.1.3 on 2024-11-07 05:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyClubUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('phone', models.CharField(max_length=20, verbose_name='Contact')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
            ],
        ),
        migrations.DeleteModel(
            name='MyClubUser',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='manager',
            field=models.CharField(max_length=20, verbose_name='Organizing Manager'),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.venue'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='venue',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Contact'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='zip_code',
            field=models.CharField(max_length=20, verbose_name='Zip Code'),
        ),
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, to='events.myclubusers'),
        ),
    ]
