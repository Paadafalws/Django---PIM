# Generated by Django 4.1.7 on 2023-03-12 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(max_length=255)),
                ('valor', models.CharField(max_length=255)),
            ],
        ),
    ]