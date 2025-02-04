# Generated by Django 2.2.24 on 2023-01-06 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0002_auto_20190829_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
        migrations.AddField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(null=True, verbose_name='Новостройка'),
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст жалобы')),
                ('flat', models.ForeignKey(related_name='complaints', max_length=10, on_delete=django.db.models.deletion.CASCADE, to='property.Flat', verbose_name='Квартира на которую пожаловались:')),
                ('user', models.ForeignKey(related_name='complaints', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался:')),
            ],
        ),
    ]
