# Generated by Django 5.1.5 on 2025-01-29 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0003_alter_trainer_payment_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='payment_amount',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='payment_date',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='payment_status',
        ),
    ]
