# Generated by Django 2.0.6 on 2019-02-21 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='citizen',
            name='residentState',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='momState_app.State'),
        ),
        migrations.AddField(
            model_name='child',
            name='mother',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='momState_app.Mom'),
        ),
    ]