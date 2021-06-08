# Generated by Django 3.2.4 on 2021-06-08 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0003_delete_helprequest'),
        ('medic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medic_notes', models.TextField()),
                ('patient_notes', models.TextField()),
                ('patient_location', models.CharField(max_length=120)),
                ('time_requested', models.DateTimeField(auto_now_add=True)),
                ('time_accepted', models.DateTimeField()),
                ('time_concluded', models.DateTimeField()),
                ('medic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medic.medic')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
