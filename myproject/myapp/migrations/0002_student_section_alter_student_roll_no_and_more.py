# Generated by Django 5.0.7 on 2024-07-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='section',
            field=models.CharField(default='A', max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_class',
            field=models.CharField(max_length=10),
        ),
    ]
