# Generated by Django 4.0.5 on 2022-07-01 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduceapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geust',
            name='body',
            field=models.TextField(),
        ),
    ]
