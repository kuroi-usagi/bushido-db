# Generated by Django 4.1.1 on 2022-10-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bushido', '0009_alter_kifeat_timing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kifeat',
            name='timing',
            field=models.CharField(choices=[('Active', 'Active'), ('Instant', 'Instant'), ('Simple', 'Simple'), ('Complex', 'Complex')], default='A', max_length=8),
        ),
    ]