# Generated by Django 3.0.3 on 2020-07-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumedCalorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('total_calorie', models.IntegerField(default=0)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='nutrtionfactslabel',
            name='serving_size',
            field=models.IntegerField(default=100, help_text='Serving size in grams.'),
        ),
    ]