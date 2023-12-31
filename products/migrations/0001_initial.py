# Generated by Django 4.2.7 on 2023-11-12 14:46

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Collectable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('sku', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('year', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.genre')),
                ('platform', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.platform')),
            ],
        ),
    ]
