# Generated by Django 5.0.4 on 2024-05-15 16:26

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=255)),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(upload_to='product_images/')),
                ('description', models.TextField()),
                ('base_metal', models.CharField(max_length=100)),
                ('stone_type', models.CharField(max_length=100)),
                ('sizing', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('plating', models.CharField(max_length=100)),
                ('country_of_origin', models.CharField(max_length=100)),
                ('quantity_in_stock', models.PositiveIntegerField(default=0)),
                ('reorder_level', models.PositiveIntegerField(default=0)),
                ('cost', models.DecimalField(decimal_places=2, default=100, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TotalAmount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('PurchaseOrderDate', models.DateField()),
                ('Status', models.CharField(blank=True, max_length=250)),
                ('ExpectedDeliveryDate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(default='customer', max_length=50)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recepient_name', models.CharField(max_length=100, null=True)),
                ('recepient_contact', models.CharField(max_length=20, null=True)),
                ('address_line1', models.CharField(max_length=255)),
                ('address_line2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jewellery_app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Placed', 'placed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Pending', max_length=20)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewellery_app.address')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewellery_app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewellery_app.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewellery_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewellery_app.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewellery_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryProduct',
            fields=[
            ],
            options={
                'verbose_name': 'Inventory',
                'verbose_name_plural': 'Inventory',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('jewellery_app.product',),
        ),
        migrations.CreateModel(
            name='PurchaseOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('PurchaseUnitPrice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('TotalAmount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewellery_app.product')),
                ('PurchaseOrder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewellery_app.purchaseorder')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_no', models.CharField(max_length=12, unique=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('address', models.CharField(max_length=255)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='Seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewellery_app.seller'),
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewellery_app.seller'),
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=100)),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewellery_app.category')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewellery_app.subcategory'),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewellery_app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
