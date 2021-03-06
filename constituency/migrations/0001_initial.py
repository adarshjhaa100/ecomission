# Generated by Django 2.2 on 2019-04-06 20:42

import constituency.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pollingStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='aaaa', max_length=100)),
                ('photo', models.ImageField(upload_to=constituency.models.user_path)),
                ('lat', models.FloatField(default=0.0)),
                ('lon', models.FloatField(default=0.0)),
                ('people', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('no', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='suggest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion', models.CharField(max_length=250)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epicNo', models.CharField(default='null', max_length=10)),
                ('const', models.CharField(max_length=30)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constituency.pollingStation')),
            ],
        ),
        migrations.CreateModel(
            name='pwd_voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epicNo', models.CharField(default='null', max_length=10)),
                ('const', models.CharField(max_length=20)),
                ('category', models.CharField(default='PWD', max_length=4)),
                ('ph', models.BigIntegerField(default=0)),
                ('plat', models.FloatField(default=0.0)),
                ('plon', models.FloatField(default=0.0)),
                ('pick', models.DateTimeField(default=django.utils.timezone.now)),
                ('drop', models.DateTimeField(default=django.utils.timezone.now)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constituency.pollingStation')),
            ],
        ),
        migrations.CreateModel(
            name='facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constituency.pollingStation')),
            ],
        ),
    ]
