# Generated by Django 3.2.3 on 2021-06-25 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ApplicationForm', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='admission',
            fields=[
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ApplicationForm.application_form_model', verbose_name='Register Name')),
                ('room_no', models.CharField(max_length=5, verbose_name='Room Number')),
            ],
        ),
    ]