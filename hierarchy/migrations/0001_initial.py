# Generated by Django 3.2.3 on 2021-05-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('sl_no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('parent_id', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Relations',
            },
        ),
    ]
