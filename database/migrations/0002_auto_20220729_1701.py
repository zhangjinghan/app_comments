# Generated by Django 3.2.5 on 2022-07-29 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentslist',
            name='msgid',
            field=models.CharField(default='nan', max_length=255),
        ),
        migrations.AlterField(
            model_name='commentslist',
            name='content',
            field=models.CharField(default='nan', max_length=255),
        ),
        migrations.AlterField(
            model_name='commentslist',
            name='date',
            field=models.CharField(default='000000', max_length=255),
        ),
        migrations.AlterField(
            model_name='commentslist',
            name='name',
            field=models.CharField(default='outlook', max_length=255),
        ),
        migrations.AlterField(
            model_name='commentslist',
            name='score',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='commentslist',
            name='user',
            field=models.CharField(default='anoy', max_length=255),
        ),
        migrations.AlterField(
            model_name='commentslist',
            name='version',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]