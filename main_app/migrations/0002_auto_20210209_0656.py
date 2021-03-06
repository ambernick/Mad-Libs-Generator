# Generated by Django 3.1.6 on 2021-02-09 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='madlib',
            name='age',
        ),
        migrations.RemoveField(
            model_name='madlib',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='madlib',
            name='description',
        ),
        migrations.RemoveField(
            model_name='madlib',
            name='name',
        ),
        migrations.AddField(
            model_name='madlib',
            name='story',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='madlib',
            name='theme',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='madlib',
            name='title',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='madlib',
            name='wordinserts',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
