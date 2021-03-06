# Generated by Django 3.2.9 on 2021-11-10 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0004_auto_20211110_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Social Media Links',
                'verbose_name_plural': 'Social Media Links',
            },
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='social_media_links',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webApp.socialmedialink'),
        ),
    ]
