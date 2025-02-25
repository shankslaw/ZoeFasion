# Generated by Django 5.0.7 on 2024-07-29 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdt_name', models.CharField(max_length=100)),
                ('pdt_image', models.ImageField(upload_to='Images')),
                ('pdt_price', models.IntegerField()),
                ('pdt_description', models.TextField()),
                ('pdt_brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brand', to='Home.productbrand')),
            ],
        ),
    ]
