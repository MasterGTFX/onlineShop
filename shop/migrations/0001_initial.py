# Generated by Django 3.0 on 2019-12-30 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('add_date', models.DateField()),
            ],
        ),
    ]
