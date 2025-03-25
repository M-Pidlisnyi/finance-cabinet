# Generated by Django 5.1.7 on 2025-03-25 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debitaccount',
            name='default_cashback',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='default cashback (%)'),
        ),
        migrations.AlterField(
            model_name='debitaccount',
            name='default_commission',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='default commission (%)'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='interest_rate',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='interest rate (%)'),
        ),
    ]
