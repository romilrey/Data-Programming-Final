# Generated by Django 4.1 on 2022-08-09 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('rate_dict', models.CharField(blank=True, max_length=10, null=True)),
                ('slug', models.SlugField(default='test')),
            ],
        ),
    ]
