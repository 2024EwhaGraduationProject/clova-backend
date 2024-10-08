# Generated by Django 5.1 on 2024-08-17 09:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0003_delete_location'),
        ('lostitem', '0004_alter_lost_category_alter_lost_getwhere_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(unique=True)),
                ('AnnouncementDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('contents', models.TextField(unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
