# Generated by Django 4.1.6 on 2023-02-10 02:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cashapp', '0008_alter_order_email_alter_order_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='qr_url',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='QR URL'),
        ),
        migrations.AlterField(
            model_name='order',
            name='tickets_count',
            field=models.IntegerField(max_length=10, verbose_name='Ticket count'),
        ),
    ]
