# Generated by Django 5.0.3 on 2024-04-03 11:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('position', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=2000, null=True)),
                ('salary', models.IntegerField(null=True)),
                ('experience', models.IntegerField(null=True)),
                ('Location', models.CharField(max_length=2000, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], max_length=200, null=True)),
                ('mobile', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('resume', models.FileField(null=True, upload_to='')),
                ('company', models.ManyToManyField(blank=True, to='JobPortal.company')),
            ],
        ),
    ]
