# Generated by Django 4.2.4 on 2023-08-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="key1",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AddField(
            model_name="blog",
            name="key2",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AddField(
            model_name="blog",
            name="key3",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AddField(
            model_name="blog",
            name="pic1",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="blog",
            name="pic2",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="blog",
            name="pic3",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="blog",
            name="pic4",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="blog",
            name="pic5",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="blog",
            name="source",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AddField(
            model_name="blog",
            name="time",
            field=models.CharField(default="", max_length=20),
        ),
        migrations.AlterField(
            model_name="blog",
            name="title",
            field=models.CharField(max_length=50),
        ),
    ]
