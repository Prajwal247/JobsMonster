# Generated by Django 3.1.5 on 2021-01-17 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hiring', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiringinfo',
            name='Full_name',
            field=models.CharField(help_text='Your Full name', max_length=200),
        ),
        migrations.AlterField(
            model_name='hiringinfo',
            name='Required_for',
            field=models.CharField(help_text='Must be the area in which he/she is expert in', max_length=100),
        ),
        migrations.AlterField(
            model_name='hiringinfo',
            name='address',
            field=models.CharField(help_text='address must be valid and genuine', max_length=50),
        ),
        migrations.AlterField(
            model_name='hiringinfo',
            name='contact_no',
            field=models.CharField(help_text='Contact no of yours', max_length=14),
        ),
        migrations.AlterField(
            model_name='hiringinfo',
            name='date',
            field=models.DateField(help_text='Date for the reservation'),
        ),
        migrations.AlterField(
            model_name='hiringinfo',
            name='description',
            field=models.TextField(help_text='Full description of the work'),
        ),
        migrations.AlterField(
            model_name='hiringinfo',
            name='estimated_duration',
            field=models.FloatField(help_text='For how many hour do you need him/her'),
        ),
    ]