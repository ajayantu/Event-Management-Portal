# Generated by Django 3.2.3 on 2021-05-26 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0016_delete_registerevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='cordinator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cord_username', models.CharField(max_length=50)),
            ],
        ),
    ]
