# Generated by Django 5.0.3 on 2024-07-07 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_receipe_user_alter_receipe_receipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='receipe_ingredients',
            field=models.TextField(blank=True, null=True),
        ),
    ]
