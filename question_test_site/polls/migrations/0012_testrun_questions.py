# Generated by Django 3.2.5 on 2021-08-04 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20210805_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='testrun',
            name='questions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.question'),
        ),
    ]
