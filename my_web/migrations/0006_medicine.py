# Generated by Django 2.1.7 on 2019-05-06 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_web', '0005_student_studentunion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=20)),
                ('medicine_num', models.IntegerField()),
            ],
        ),
    ]
