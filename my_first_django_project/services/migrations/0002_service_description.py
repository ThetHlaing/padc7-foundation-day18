# Generated by Django 2.2.4 on 2019-08-04 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description of the service'),
        ),
    ]
