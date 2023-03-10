# Generated by Django 4.1.1 on 2022-10-01 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_remove_product_kind"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="kind",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product",
                to="products.productkind",
            ),
            preserve_default=False,
        ),
    ]