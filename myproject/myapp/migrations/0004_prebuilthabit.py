# Generated by Django 4.1.7 on 2023-04-03 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_habit_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrebuiltHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
