# Generated by Django 4.1.7 on 2023-04-19 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='showdid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('did', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'dealer',
            },
        ),
    ]
