# Generated by Django 4.2.5 on 2023-11-26 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='posicion',
            field=models.ForeignKey(default='stash', on_delete=django.db.models.deletion.CASCADE, to='core.posiciones'),
        ),
    ]