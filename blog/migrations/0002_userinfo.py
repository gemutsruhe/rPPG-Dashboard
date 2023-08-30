# Generated by Django 4.2.4 on 2023-08-29 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('timestamp', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=30)),
                ('sex', models.TextField(max_length=1)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
