# Generated by Django 2.1.7 on 2019-04-04 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_boy_girl_love'),
    ]

    operations = [
        migrations.CreateModel(
            name='happy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
