# Generated by Django 3.2 on 2021-04-20 10:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('product_name', models.CharField(blank=True, max_length=255, null=True)),
                ('product_description', models.TextField(max_length=255, null=True)),
                ('secret_description', models.TextField(max_length=255, null=True)),
                ('price', models.FloatField(default=0)),
                ('currency', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('status_of_transaction', models.IntegerField(choices=[(0, 'Progress'), (-1, 'Cancelled'), (1, 'Success')], default=0)),
                ('expected_value', models.IntegerField(null=True)),
                ('received_value', models.IntegerField(blank=True, null=True)),
                ('txid', models.TextField(null=True)),
                ('address', models.TextField(null=True)),
                ('order_id', models.TextField(null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('crypto', models.CharField(choices=[('BTC', 'Btc'), ('BCH', 'Bch')], max_length=255, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='core.product')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('file_data', models.BinaryField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='core.product')),
            ],
        ),
    ]