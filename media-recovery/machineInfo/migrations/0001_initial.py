# Generated by Django 4.2.5 on 2023-10-04 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BootboxDriveDisk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diskLocationUnit', models.CharField(max_length=5)),
                ('totalVolume', models.CharField(max_length=25)),
                ('usedVolume', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=25)),
                ('serialNumber', models.CharField(max_length=25, unique=True)),
                ('machineTypeModel', models.CharField(max_length=16)),
                ('biosVersion', models.CharField(max_length=16)),
                ('biosReleaseDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(max_length=25)),
                ('plataform', models.CharField(max_length=25)),
                ('version', models.CharField(max_length=25)),
                ('edition', models.CharField(max_length=25)),
                ('size', models.CharField(max_length=25)),
                ('lastUpdate', models.CharField(max_length=25)),
                ('Language', models.CharField(max_length=25)),
                ('bootbox', models.ForeignKey(blank=True, default=None, max_length=25, null=True, on_delete=django.db.models.deletion.SET_NULL, to='machineInfo.bootboxdrivedisk')),
            ],
        ),
        migrations.CreateModel(
            name='DriveDisk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driveName', models.CharField(max_length=25)),
                ('serialNumber', models.CharField(max_length=25)),
                ('Interface', models.CharField(max_length=25)),
                ('diskLocationUnit', models.CharField(max_length=5)),
                ('totalVolume', models.CharField(max_length=25)),
                ('usedVolume', models.CharField(max_length=25)),
                ('machine', models.ForeignKey(blank=True, default=None, max_length=25, null=True, on_delete=django.db.models.deletion.SET_NULL, to='machineInfo.machine')),
            ],
        ),
    ]
