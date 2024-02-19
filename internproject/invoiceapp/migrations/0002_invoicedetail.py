# Generated by Django 4.2.10 on 2024-02-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_id', models.IntegerField()),
                ('description', models.CharField(max_length=400)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('price', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
    ]
