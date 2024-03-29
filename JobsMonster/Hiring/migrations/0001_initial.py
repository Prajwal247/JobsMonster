# Generated by Django 3.1.5 on 2021-02-27 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HiringInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(help_text='Your Full name', max_length=200)),
                ('address', models.CharField(help_text='address must be valid and genuine', max_length=50)),
                ('date', models.DateField(help_text='Date for the reservation')),
                ('Required_for', models.CharField(help_text='Must be the area in which he/she is expert in', max_length=100)),
                ('description', models.TextField(help_text='Full description of the work')),
                ('estimated_duration', models.FloatField(help_text='For how many hour do you need him/her')),
                ('contact_no', models.CharField(help_text='Contact no of yours', max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Jobpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('category', models.CharField(choices=[('Recruiter', 'Recruiter'), ('Agriculture,Food and Natural Resources', 'Agriculture,Food and Natural Resources'), ('Architecture and Construction', 'Architecture and Construction'), ('Technology and Communications', 'Technology and Communications'), ('Business Management and Administration', 'Business Management and Administration'), ('Education and Training', 'Education and Training'), ('Finance', 'Finance'), ('Government and Public Administration', 'Government and Public Administration'), ('Health Science', 'Health Science'), ('Hospitality and Tourism', 'Hospitality and Tourism'), ('Human Service', 'Humanservice'), ('Information Technology', 'Information Technology'), ('Law and Pulblic Safety', 'Law and Pulblic Safety'), ('Manufacturing', 'Manufacturing'), ('Sales and Marketing', 'Sales and Marketing'), ('Engineering and Mathematics', 'Engineering and Mathematics'), ('Transportation', 'Transportation')], max_length=100)),
                ('estimated_time', models.IntegerField(help_text='required time to complete the job in hr')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_date', models.DateField()),
                ('jobpost_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hiring.jobpost')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
