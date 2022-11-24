# Generated by Django 4.1.3 on 2022-11-23 09:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('content', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=70)),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projboard.article')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projboard.user')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projboard.article')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projboard.user')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='subject_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projboard.subject'),
        ),
        migrations.AddField(
            model_name='article',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projboard.user'),
        ),
    ]