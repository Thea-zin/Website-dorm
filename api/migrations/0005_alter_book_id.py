# Generated by Django 4.2.3 on 2023-08-08 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_book_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
