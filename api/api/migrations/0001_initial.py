# Generated by Django 3.0.3 on 2020-03-04 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.DecimalField(decimal_places=0, max_digits=38, primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('usertype', models.TextField()),
                ('usertypeid', models.DecimalField(decimal_places=0, max_digits=38)),
            ],
        ),
    ]
