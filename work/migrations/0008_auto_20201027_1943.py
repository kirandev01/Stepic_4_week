# Generated by Django 3.1.2 on 2020-10-27 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0007_auto_20201027_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, upload_to='company_images', verbose_name='Логотип'),
        ),
    ]