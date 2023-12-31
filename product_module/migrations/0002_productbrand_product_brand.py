# Generated by Django 4.2.4 on 2023-08-31 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Brand Name')),
                ('is_active', models.BooleanField(verbose_name='Active/Not Active')),
            ],
            options={
                'verbose_name': 'Brands',
                'verbose_name_plural': 'Brand Name',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product_module.productbrand', verbose_name='Brand Name'),
        ),
    ]
