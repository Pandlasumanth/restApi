# Generated by Django 2.1.4 on 2018-12-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcareapp', '0003_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=200)),
                ('Message', models.CharField(max_length=500)),
            ],
        ),
    ]