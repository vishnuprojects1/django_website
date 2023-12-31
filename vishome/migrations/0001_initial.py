# Generated by Django 4.1.7 on 2023-06-02 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("proname", models.CharField(max_length=50)),
                ("prospec", models.CharField(max_length=50)),
                ("proprice", models.IntegerField(default=0)),
                ("proimg", models.ImageField(max_length=50, upload_to="")),
            ],
        ),
    ]
