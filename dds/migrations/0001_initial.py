# Generated by Django 3.1 on 2021-07-04 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfExpenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summa', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comment', models.TextField(blank=True, null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dds.typeofexpenses')),
            ],
        ),
    ]
