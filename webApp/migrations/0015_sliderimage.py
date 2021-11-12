# Generated by Django 3.2.9 on 2021-11-12 09:41

from django.db import migrations, models
import django.db.models.deletion
import webApp.models.slider_image


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0014_alter_companyprofile_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('subtitle', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to=webApp.models.slider_image.create_path_slider_image)),
                ('company', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webApp.companyprofile')),
            ],
        ),
    ]