# Generated by Django 3.1.3 on 2020-11-30 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0008_delete_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yr', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_code', models.CharField(max_length=100)),
                ('sub_name', models.CharField(max_length=100)),
                ('semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='calc.semester')),
                ('year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='calc.year')),
            ],
        ),
        migrations.AddField(
            model_name='semester',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calc.year'),
        ),
    ]
