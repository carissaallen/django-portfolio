# Generated by Django 2.1.7 on 2019-02-27 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190227_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pubdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
