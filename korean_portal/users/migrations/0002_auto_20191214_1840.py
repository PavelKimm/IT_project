# Generated by Django 3.0 on 2019-12-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]
