# Generated by Django 2.2.24 on 2023-01-07 09:04

from django.db import migrations
import phonenumbers


def gets_normalized_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    owners = Flat.objects.all()
    for owner in owners.iterator():
        ru_phonenumber = phonenumbers.parse(owner.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(ru_phonenumber):
            phone_number_format = phonenumbers.format_number(
                ru_phonenumber,
                phonenumbers.PhoneNumberFormat.E164
            )
            owner.owner_pure_phone = phone_number_format
            owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(gets_normalized_numbers)
    ]
