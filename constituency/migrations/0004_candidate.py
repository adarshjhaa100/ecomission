# Generated by Django 2.2 on 2019-04-07 09:24

import constituency.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constituency', '0003_auto_20190407_0215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('party', models.CharField(max_length=10)),
                ('symbol', models.ImageField(upload_to=constituency.models.user_path)),
                ('affitavid', models.ImageField(upload_to=constituency.models.user_path)),
            ],
        ),
    ]