# Generated by Django 3.2.4 on 2021-07-17 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0011_auto_20210716_0500'),
    ]

    operations = [
        migrations.CreateModel(
            name='itemlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=64)),
                ('ammount', models.CharField(max_length=64)),
                ('vendor', models.CharField(max_length=64)),
            ],
        ),
    ]