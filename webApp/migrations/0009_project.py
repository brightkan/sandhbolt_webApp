# Generated by Django 3.2.9 on 2021-11-10 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0008_review_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('started', models.DateField()),
                ('ended', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=40)),
                ('picture', models.ImageField(upload_to='')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webApp.client')),
            ],
        ),
    ]