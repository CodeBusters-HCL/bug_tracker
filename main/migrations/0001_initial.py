# Generated by Django 3.1.1 on 2020-09-28 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug_category', models.CharField(max_length=200)),
                ('bug_summary', models.TextField(max_length=200)),
                ('bug_severity', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('critical', 'Critical')], default='low', max_length=8)),
                ('bug_desc', models.TextField(max_length=500)),
                ('bug_status', models.CharField(choices=[('assigned', 'Assigned'), ('unassigned', 'UnAssigned'), ('waiting_for_response', 'Waiting for Response'), ('dropped', 'Dropped')], default='unassigned', max_length=20)),
                ('date_reported', models.DateTimeField(verbose_name='date_published')),
            ],
        ),
    ]
