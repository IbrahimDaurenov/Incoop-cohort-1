# Generated by Django 3.0.2 on 2020-08-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('animals', models.ManyToManyField(blank=True, to='animal.Animal')),
            ],
        ),
    ]
