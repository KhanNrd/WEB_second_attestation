# Generated by Django 2.0.3 on 2018-04-20 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
