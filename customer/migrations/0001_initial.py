# Generated by Django 5.1.6 on 2025-03-06 03:52

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
            name='students_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_img', models.ImageField(upload_to='student_uploads/')),
                ('student_name', models.CharField(max_length=200)),
                ('student_mob', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('student_email', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('student_education', models.CharField(blank=True, max_length=100, null=True)),
                ('student_about', models.TextField(default='About Me', null=True)),
                ('student_rented_books', models.TextField(blank=True, null=True)),
                ('student_created_at', models.DateTimeField(auto_now=True)),
                ('student_update_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
