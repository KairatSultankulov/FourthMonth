# Generated by Django 4.2.19 on 2025-03-18 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('films', '0006_alter_reviews_options_alter_reviews_choice_film_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('✅', '✅'), ('❌', '❌')], default='❌', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('choice_films', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.films')),
            ],
        ),
    ]
