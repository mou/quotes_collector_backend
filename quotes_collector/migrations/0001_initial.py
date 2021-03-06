# Generated by Django 2.1.7 on 2019-03-17 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes_collector.Author')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('authors', models.ManyToManyField(to='quotes_collector.Author')),
            ],
        ),
        migrations.AddField(
            model_name='quote',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes_collector.Source'),
        ),
        migrations.AddField(
            model_name='author',
            name='sources',
            field=models.ManyToManyField(to='quotes_collector.Source'),
        ),
    ]
