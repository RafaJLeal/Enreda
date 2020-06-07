# Generated by Django 2.2.2 on 2019-07-14 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the user's name.", max_length=150, verbose_name="User's name")),
                ('email', models.EmailField(help_text="Enter the email's name.", max_length=254, verbose_name="Email's name")),
            ],
        ),
    ]