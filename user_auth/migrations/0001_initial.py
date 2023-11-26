# Generated by Django 4.1.13 on 2023-11-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('phone_code', models.CharField(max_length=5)),
                ('phone_number', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('country', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=128)),
                ('groups', models.ManyToManyField(related_name='user_auth_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='user_auth_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
