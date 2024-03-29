# Generated by Django 2.1.7 on 2019-06-02 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payload', models.PositiveIntegerField(default=0, verbose_name='车上人数')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('location', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Site')),
            ],
        ),
        migrations.CreateModel(
            name='WJ',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('q1', models.BooleanField(default=True, verbose_name='是否需要公共交通')),
                ('q2', models.CharField(choices=[('minibus', '小型公交车'), ('ecar', '电瓶车'), ('railway', '轨道交通')], max_length=8, verbose_name='交通方式')),
                ('q3', models.CharField(max_length=32, verbose_name='现在在何处')),
                ('q4', models.CharField(max_length=32, verbose_name='去往何处')),
                ('q5', models.TextField(verbose_name='最希望开通的路线')),
                ('q6', models.CharField(max_length=16, verbose_name='最希望开通的时间段')),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='stations',
            field=models.ManyToManyField(to='app.Station'),
        ),
        migrations.AddField(
            model_name='bus',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Route'),
        ),
        migrations.AddField(
            model_name='bus',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Station'),
        ),
    ]
