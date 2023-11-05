# Generated by Django 4.2.4 on 2023-08-31 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0002_alter_contact_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='fullname',
            field=models.CharField(max_length=300, verbose_name='FullName'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='is_read_by_admin',
            field=models.BooleanField(verbose_name='YES/NO'),
        ),
    ]