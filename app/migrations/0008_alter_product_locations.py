# Generated by Django 4.0.1 on 2022-01-20 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_item_remove_list_product_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='locations',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='app.location'),
        ),
    ]
