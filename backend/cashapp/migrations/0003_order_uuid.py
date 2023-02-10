# Generated by Django 4.1.6 on 2023-02-09 23:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('cashapp', '0002_order_qr_id_order_qr_status_order_qr_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid1, editable=False),
        ),
    ]
