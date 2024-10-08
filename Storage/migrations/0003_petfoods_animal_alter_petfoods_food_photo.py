# Generated by Django 5.1.1 on 2024-09-25 21:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Storage', '0002_petfoods_food_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='petfoods',
            name='animal',
            field=models.CharField(choices=[('Cão', 'dog'), ('Gato', 'cat')], default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='petfoods',
            name='food_photo',
            field=models.ImageField(blank=True, null=True, upload_to='foods/'),
        ),
    ]
