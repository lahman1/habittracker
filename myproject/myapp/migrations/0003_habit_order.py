# Generated by Django 4.1.7 on 2023-04-03 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_habit_habitentry_delete_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]