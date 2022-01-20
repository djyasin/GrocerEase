# Generated by Django 4.0.1 on 2022-01-20 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_list_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='item_quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.RemoveField(
            model_name='list',
            name='products',
        ),
        migrations.AddField(
            model_name='list',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='app.product'),
        ),
        migrations.AddConstraint(
            model_name='list',
            constraint=models.UniqueConstraint(fields=('products', 'item_quantity'), name='product_quantity'),
        ),
    ]
