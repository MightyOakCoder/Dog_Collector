# Generated by Django 4.1.3 on 2023-01-14 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='age',
        ),
        migrations.AddField(
            model_name='dog',
            name='famous_for',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]
