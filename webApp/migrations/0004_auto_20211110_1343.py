# Generated by Django 3.2.9 on 2021-11-10 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0003_companyprofile_contact_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='xcod',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='ycod',
            field=models.FloatField(blank=True, null=True),
        ),
    ]