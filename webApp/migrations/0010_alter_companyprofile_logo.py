# Generated by Django 3.2.9 on 2021-11-11 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0009_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='logo',
            field=models.ImageField(upload_to=''),
        ),
    ]