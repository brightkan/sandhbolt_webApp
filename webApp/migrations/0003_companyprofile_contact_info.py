# Generated by Django 3.2.9 on 2021-11-10 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0002_auto_20211110_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='contact_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webApp.contactinfo'),
        ),
    ]
