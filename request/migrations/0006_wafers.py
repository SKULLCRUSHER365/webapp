# Generated by Django 3.2.4 on 2021-07-05 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0005_casno'),
    ]

    operations = [
        migrations.CreateModel(
            name='wafers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=64)),
            ],
        ),
    ]
