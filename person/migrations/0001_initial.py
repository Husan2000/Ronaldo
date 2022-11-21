# Generated by Django 3.2.13 on 2022-06-13 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='author')),
                ('birthday', models.DateField()),
                ('bio', models.TextField(blank=True, null=True)),
                ('address', models.CharField(max_length=255)),
                ('zip_code', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=255)),
                ('projects', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='icon')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('is_skill', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects')),
                ('link', models.URLField(blank=True, null=True)),
                ('profession', models.CharField(max_length=255)),
                ('category', models.ManyToManyField(blank=True, to='post.Category')),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(blank=True, max_length=255, null=True)),
                ('start_finish', models.CharField(blank=True, max_length=255, null=True)),
                ('academy', models.CharField(blank=True, max_length=255, null=True)),
                ('icon', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Skill name')),
                ('percent', models.IntegerField(blank=True, null=True)),
                ('is_main', models.BooleanField(default=False)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.resume')),
            ],
        ),
    ]