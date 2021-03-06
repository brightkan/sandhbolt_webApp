# Generated by Django 3.2.9 on 2021-11-10 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0006_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=40)),
                ('rating', models.IntegerField()),
                ('client', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webApp.client')),
            ],
        ),
    ]
