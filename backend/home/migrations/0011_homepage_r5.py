# Generated by Django 2.2.12 on 2020-06-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0010_homepage_r4"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="r5",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
