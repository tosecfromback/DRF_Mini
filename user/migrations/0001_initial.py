# Generated by Django 4.2.3 on 2023-08-01 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=155, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('daily_post', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
