# Generated by Django 4.0.1 on 2022-01-16 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0021_remove_price_plan_price_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pose',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
