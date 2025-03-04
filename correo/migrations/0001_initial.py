# Generated by Django 4.2.10 on 2024-05-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('sender', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('zip_file', models.FileField(blank=True, null=True, upload_to='emails/')),
            ],
        ),
    ]
