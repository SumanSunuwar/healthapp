# Generated by Django 3.2.9 on 2021-12-02 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_patient_name'),
        ('createorders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.patient'),
        ),
    ]
