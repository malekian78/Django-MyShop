# Generated by Django 4.2.6 on 2024-01-16 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_ordermodel_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemmodel',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='order.ordermodel'),
        ),
    ]