# Generated by Django 3.2.4 on 2021-06-27 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.ManyToManyField(related_name='student_list', to='api_app.Batch'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_list', to='api_app.batch'),
        ),
    ]
