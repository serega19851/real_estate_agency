# Generated by Django 2.2.24 on 2023-01-06 13:40

from django.db import migrations


def gets_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)
    Flat.objects.filter(construction_year__lt=2015).update(new_building=False)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20230106_1615'),
    ]

    operations = [
        migrations.RunPython(gets_new_building)
    ]
