# Generated by Django 5.1.1 on 2024-10-25 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bath', '0004_alter_allpets_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monthlyplans',
            old_name='pla_phone',
            new_name='plan_phone',
        ),
    ]