# Generated by Django 5.0.1 on 2024-03-16 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branchData', '0005_alter_branchtype_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
