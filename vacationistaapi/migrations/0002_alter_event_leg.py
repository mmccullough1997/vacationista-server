# Generated by Django 4.1.7 on 2023-02-18 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacationistaapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='leg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacationistaapi.leg'),
        ),
    ]
