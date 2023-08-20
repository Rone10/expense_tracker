# Generated by Django 4.2.4 on 2023-08-19 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Groceries', 'Groceries'), ('Personal', 'Personal'), ('Other', 'Other')], max_length=100),
        ),
    ]