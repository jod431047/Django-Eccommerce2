# Generated by Django 4.2.4 on 2023-10-15 22:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_cartdetail_price_alter_cartdetail_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]