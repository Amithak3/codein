# Generated by Django 4.2.13 on 2024-08-12 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language', models.CharField(max_length=10)),
                ('input_data', models.TextField(blank=True, null=True)),
                ('output_data', models.TextField(blank=True, null=True)),
                ('code', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('verdict', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='problem',
            name='code',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='name',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='statement',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='submitted_at',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='verdict',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='output',
        ),
        migrations.AddField(
            model_name='problem',
            name='description',
            field=models.TextField(default='Default description'),
        ),
        migrations.AddField(
            model_name='problem',
            name='title',
            field=models.CharField(default='Untitled Problem', max_length=255),
        ),
        migrations.AddField(
            model_name='solution',
            name='content',
            field=models.TextField(default='Default content'),
        ),
        migrations.AddField(
            model_name='testcase',
            name='expected_output',
            field=models.TextField(default='Default output'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='input',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
