# Generated by Django 4.0.1 on 2022-01-16 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0020_alter_price_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='plan',
        ),
        migrations.AddField(
            model_name='price',
            name='plan',
            field=models.ManyToManyField(null=True, to='health.Plan'),
        ),
    ]
