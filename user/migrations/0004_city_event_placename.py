# Generated by Django 3.2.4 on 2023-09-12 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_category_cpic'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
                ('city_picture', models.ImageField(null=True, upload_to='static/city/')),
            ],
        ),
        migrations.CreateModel(
            name='placename',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('ppic', models.ImageField(null=True, upload_to='static/Hotel/')),
                ('pdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker_name', models.CharField(max_length=200, null=True)),
                ('event_picture', models.ImageField(null=True, upload_to='static/event/')),
                ('speaker_picture', models.ImageField(null=True, upload_to='static/speaker')),
                ('price', models.IntegerField()),
                ('dprice', models.IntegerField()),
                ('event_date', models.DateField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.city')),
                ('event_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.category')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.placename')),
            ],
        ),
    ]
