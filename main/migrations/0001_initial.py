# Generated by Django 2.1.2 on 2019-03-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mquiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qdesc', models.CharField(max_length=2000)),
                ('qop1', models.CharField(max_length=500)),
                ('qop2', models.CharField(max_length=500)),
                ('qop3', models.CharField(max_length=500)),
                ('qop4', models.CharField(max_length=500)),
                ('qop5', models.CharField(max_length=500)),
                ('qhint', models.CharField(max_length=1000)),
                ('qsol', models.CharField(max_length=2000)),
            ],
        ),
    ]
