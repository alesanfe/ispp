# Generated by Django 5.0.2 on 2024-02-28 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_yer_mail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='yer_mail',
            new_name='buyer_mail',
        ),
    ]