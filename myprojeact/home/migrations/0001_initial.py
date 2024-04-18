# Generated by Django 5.0.3 on 2024-03-25 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('roll', models.IntegerField()),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=10)),
                ('dob', models.DateField()),
            ],
        ),
    ]