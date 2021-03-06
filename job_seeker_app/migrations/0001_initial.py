# Generated by Django 3.0.4 on 2020-05-28 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import job_seeker_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EducationLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_level_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Professionals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=100)),
                ('organization_type', models.CharField(choices=[('Government', 'GOVERNMENT'), ('Semi Government', 'SEMI_GOVERNMENT'), ('NGO', 'NGO'), ('Private firm', 'OTHERS'), ('International Agency', 'INTERNATIONAL_AGENCY'), ('Others', 'OTHERS')], default=True, max_length=50)),
                ('department', models.CharField(choices=[('Government', 'ACCOUNTING'), ('Bank', 'BANK'), ('Engineer', 'ENGINEER'), ('Garments', 'GARMENTS'), ('HR', 'HR'), ('Others', 'OTHERS')], default=True, max_length=50)),
                ('designation', models.CharField(max_length=100)),
                ('responsibilities', models.CharField(max_length=100)),
                ('employment_from', models.DateField(blank=True, default=False, null=True)),
                ('employment_to', models.DateField(blank=True, default=False, null=True)),
                ('company_location', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Professionals',
            },
        ),
        migrations.CreateModel(
            name='Personals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('fathers_name', models.CharField(max_length=100)),
                ('mothers_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Others', 'OTHERS')], default=True, max_length=50)),
                ('religion', models.CharField(choices=[('Islam', 'ISLAM'), ('Hinduism', 'HINDUISM'), ('Buddhism', 'BUDDHISM'), ('Christianity', 'CRISTIAN'), ('Others', 'OTHERS')], default=True, max_length=50)),
                ('nid', models.PositiveSmallIntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Personals',
            },
        ),
        migrations.CreateModel(
            name='Academics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(choices=[('DHAKA', 'DHAKA'), ('RAJSHAHI', 'RAJSHAHI'), ('COMILLA', 'COMILLA'), ('JESSORE', 'JESSORE'), ('CHITTAGONG', 'CHITTAGONG'), ('BARISHAL', 'BARISHAL'), ('SYLHET', 'SYLHET'), ('DINAJPUR', 'DINAJPUR'), ('MADRASAH', 'MADRASAH')], default='DHAKA', max_length=20)),
                ('institution', models.CharField(max_length=100)),
                ('result', models.FloatField(default=0.0)),
                ('year', models.IntegerField(default=job_seeker_app.models.current_year, verbose_name='year')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_seeker_app.Degree')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Academics',
            },
        ),
    ]
