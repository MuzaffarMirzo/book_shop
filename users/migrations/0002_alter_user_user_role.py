# Generated by Django 5.0.6 on 2024-06-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.CharField(choices=[('client', 'client'), ('users', 'users'), ('seller', 'seller ')], default='client', max_length=10),
        ),
    ]
