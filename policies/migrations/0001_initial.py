# Generated by Django 5.0.6 on 2024-06-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_id', models.CharField(max_length=20)),
                ('agent_code', models.CharField(max_length=20)),
                ('premium', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sum_assured', models.DecimalField(decimal_places=2, max_digits=10)),
                ('policy_issued_date', models.DateField()),
            ],
        ),
    ]
