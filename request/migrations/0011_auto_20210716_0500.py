# Generated by Django 3.2.4 on 2021-07-16 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0010_currency'),
    ]

    operations = [
        migrations.DeleteModel(
            name='casno',
        ),
        migrations.DeleteModel(
            name='consumable',
        ),
        migrations.DeleteModel(
            name='gases',
        ),
        migrations.DeleteModel(
            name='labsupplies',
        ),
        migrations.DeleteModel(
            name='non_consumable',
        ),
        migrations.DeleteModel(
            name='softwarelicence',
        ),
        migrations.DeleteModel(
            name='wafers',
        ),
    ]