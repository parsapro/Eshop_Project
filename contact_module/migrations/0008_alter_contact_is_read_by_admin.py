# Generated by Django 4.2.4 on 2023-09-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0007_alter_contact_is_read_by_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='is_read_by_admin',
            field=models.BooleanField(default=False, null=True, verbose_name='YES/NO'),
        ),
    ]
