# Generated by Django 2.1.3 on 2019-02-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_details',
            name='contact_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]