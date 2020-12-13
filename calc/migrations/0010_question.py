# Generated by Django 3.1.3 on 2020-11-30 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0009_auto_20201130_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=500)),
                ('op1', models.CharField(max_length=200)),
                ('op2', models.CharField(max_length=200)),
                ('op3', models.CharField(max_length=200)),
                ('op4', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.subject')),
            ],
        ),
    ]
