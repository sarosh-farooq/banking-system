# Generated by Django 2.2.7 on 2021-07-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210718_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, help_text='Postal Address', max_length=180, null=True),
        ),
    ]
