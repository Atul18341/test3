# Generated by Django 4.1.7 on 2023-02-22 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskDashboard', '0006_studentsprofile_contact_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsprofile',
            name='Certificate_Link',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='studentsprofile',
            name='College_Name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='studentsprofile',
            name='Name',
            field=models.CharField(default='', max_length=200),
        ),
    ]