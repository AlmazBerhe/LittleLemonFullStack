# Generated by Django 5.0.4 on 2024-05-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonFS', '0003_alter_menu_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='reservation_slot',
            field=models.CharField(choices=[('select time', 'select time')], default='select time', max_length=15),
        ),
    ]