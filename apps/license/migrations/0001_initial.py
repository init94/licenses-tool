# Generated by Django 2.1 on 2018-08-13 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=250)),
                ('serial', models.CharField(max_length=50)),
                ('valid_date', models.DateField()),
            ],
        ),
    ]
