# Generated by Django 5.0.2 on 2025-01-17 13:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='papers/')),
                ('title', models.CharField(max_length=255)),
                ('processed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('error_message', models.TextField(blank=True, null=True)),
                ('has_summary', models.BooleanField(default=False)),
                ('has_analysis', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PaperAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis_data', models.JSONField()),
                ('analyzed_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analyses', to='papers.paper')),
            ],
            options={
                'ordering': ['-analyzed_at'],
            },
        ),
        migrations.CreateModel(
            name='PaperSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary_data', models.JSONField()),
                ('generated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='summaries', to='papers.paper')),
            ],
            options={
                'ordering': ['-generated_at'],
            },
        ),
    ]
