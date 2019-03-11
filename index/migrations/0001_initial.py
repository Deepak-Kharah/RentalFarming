# Generated by Django 2.1.5 on 2019-03-09 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TractorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Owner_Name', models.CharField(max_length=150)),
                ('City', models.CharField(max_length=50)),
                ('Drive', models.IntegerField(max_length=1)),
                ('Hp', models.IntegerField(max_length=2)),
                ('RentPerHour', models.IntegerField(max_length=4)),
                ('Image', models.ImageField(upload_to='images/tractor/')),
            ],
        ),
    ]
