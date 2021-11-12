# Generated by Django 3.2.9 on 2021-11-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0012_alter_companyprofile_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='logo',
            field=models.ImageField(null=True, upload_to='company_profile'),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='mission',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='name',
            field=models.CharField(default='Sandhbolt', max_length=20),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='profile_pdf',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='since',
            field=models.IntegerField(default=2015),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='vision',
            field=models.TextField(null=True),
        ),
    ]
