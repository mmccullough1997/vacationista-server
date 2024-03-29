# Generated by Django 4.1.7 on 2023-03-23 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_posted', models.DateField()),
                ('content', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=500)),
                ('thumbnail', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('thumbnail', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Leg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('location', models.CharField(max_length=500)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=500)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('location', models.CharField(max_length=500)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=20)),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransportationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('travel_from', models.CharField(max_length=500)),
                ('travel_to', models.CharField(max_length=500)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('date_registered', models.DateField()),
                ('username', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=400)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TripLeg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacationistaapi.leg')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacationistaapi.trip')),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacationistaapi.user'),
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_from', models.CharField(max_length=500)),
                ('travel_to', models.CharField(max_length=500)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('comment', models.CharField(max_length=500)),
                ('round_trip', models.BooleanField()),
                ('leg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacationistaapi.leg')),
                ('transportation_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacationistaapi.transportationtype')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacationistaapi.trip')),
            ],
        ),
        migrations.AddField(
            model_name='leg',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacationistaapi.user'),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('comment', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('expense_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacationistaapi.expensetype')),
                ('leg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacationistaapi.leg')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacationistaapi.trip')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('date', models.DateField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
                ('title', models.CharField(max_length=500)),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacationistaapi.eventtype')),
                ('leg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacationistaapi.leg')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacationistaapi.trip')),
            ],
        ),
    ]
