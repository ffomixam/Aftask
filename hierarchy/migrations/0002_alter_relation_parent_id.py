# Generated by Django 3.2.3 on 2021-05-28 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='parent_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]