# Generated by Django 4.2.16 on 2024-10-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.URLField(),
        ),
    ]
