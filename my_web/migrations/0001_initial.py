# Generated by Django 2.1.7 on 2019-05-02 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-pub_data',),
            },
        ),
    ]
