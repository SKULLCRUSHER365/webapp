# Generated by Django 3.2.4 on 2021-07-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0007_gases_labsupplies_softwarelicence_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='selection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory', models.CharField(max_length=64)),
                ('subcatagory1', models.CharField(max_length=64)),
            ],
        ),
    ]