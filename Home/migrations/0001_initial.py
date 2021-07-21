# Generated by Django 3.2.2 on 2021-07-21 22:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.PositiveIntegerField()),
                ('beverage', models.BooleanField(default=False)),
                ('snack', models.BooleanField(default=False)),
                ('discontinued', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10)])),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.items')),
            ],
            options={
                'db_table': 'order_items',
            },
        ),
    ]
