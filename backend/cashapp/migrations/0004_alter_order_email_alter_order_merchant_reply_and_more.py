# Generated by Django 4.1.6 on 2023-02-09 23:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cashapp', '0003_order_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.TextField(blank=True, default='', verbose_name='Customer email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='merchant_reply',
            field=models.TextField(blank=True, default='', verbose_name='Merchant reply'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.TextField(blank=True, default='', verbose_name='Customer phone'),
        ),
        migrations.AlterField(
            model_name='order',
            name='qr_id',
            field=models.TextField(blank=True, default='', verbose_name='QR ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='qr_status',
            field=models.TextField(blank=True, default='', verbose_name='QR Status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='qr_url',
            field=models.TextField(blank=True, default='', verbose_name='QR URL'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.TextField(blank=True, default='', verbose_name='Order status'),
        ),
    ]