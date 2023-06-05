# Generated by Django 4.1.1 on 2022-10-05 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bushido', '0005_alter_kifeat_cost_alter_unit_kimax_alter_unit_kistat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='kiBoost',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AddField(
            model_name='unit',
            name='meleeBoost',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AddField(
            model_name='unit',
            name='moveBoost',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AddField(
            model_name='unit',
            name='rangedBoost',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AddField(
            model_name='unit',
            name='size',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='unit',
            name='wounds',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='unit',
            name='kiMax',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='unit',
            name='kiStat',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='unit',
            name='meleePool',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='unit',
            name='movePool',
            field=models.CharField(default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='unit',
            name='rangedPool',
            field=models.CharField(default='0', max_length=3),
        ),
    ]