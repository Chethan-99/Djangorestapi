# Generated by Django 3.2.8 on 2021-10-08 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangorestAPIapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='John', max_length=50),
        ),
    ]
