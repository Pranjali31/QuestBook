# Generated by Django 4.1.7 on 2023-03-24 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_destination_detailed_desc_delete_adventure_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detailed_desc',
            options={'verbose_name_plural': 'Detailed descriptions'},
        ),
    ]
