# Generated by Django 3.2.3 on 2021-05-22 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0003_makeevent_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makeevent',
            name='event_poster',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]