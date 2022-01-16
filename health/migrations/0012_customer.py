# Generated by Django 4.0.1 on 2022-01-15 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0011_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='customerphoto')),
                ('review', models.TextField(max_length=200)),
            ],
        ),
    ]