# Generated by Django 2.1 on 2018-08-06 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookShop', '0002_auto_20180806_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
