# Generated by Django 3.2.9 on 2022-02-11 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_auto_20220211_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='resume',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]