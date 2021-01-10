# Generated by Django 3.1.5 on 2021-01-10 05:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='dob',
            new_name='DOB',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='gender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='nationality',
            new_name='Nationality',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_freelancer',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='static/img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
