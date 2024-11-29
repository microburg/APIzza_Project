# Generated by Django 5.1.3 on 2024-11-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('items', models.TextField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
    ]
