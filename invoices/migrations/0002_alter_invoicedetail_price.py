# Generated by Django 5.0.1 on 2024-01-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetail',
            name='price',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10),
        ),
    ]