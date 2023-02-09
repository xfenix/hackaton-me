# Generated by Django 4.1.6 on 2023-02-09 20:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cashapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='qr_id',
            field=models.TextField(default='', verbose_name='QR ID'),
        ),
        migrations.AddField(
            model_name='order',
            name='qr_status',
            field=models.TextField(default='', verbose_name='QR Status'),
        ),
        migrations.AddField(
            model_name='order',
            name='qr_url',
            field=models.TextField(default='', verbose_name='QR URL'),
        ),
        migrations.AddField(
            model_name='organization',
            name='merchant_id',
            field=models.TextField(default='', verbose_name='Merchant id'),
        ),
        migrations.AlterField(
            model_name='eventqrcode',
            name='alias',
            field=models.TextField(unique=True, verbose_name='QR Code alias'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.TextField(default='', verbose_name='Customer email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='merchant_reply',
            field=models.TextField(default='', verbose_name='Merchant reply'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.TextField(default='', verbose_name='Customer phone'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.TextField(default='', verbose_name='Order status'),
        ),
    ]