# Generated by Django 4.2.16 on 2024-11-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Заголовок')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('tetx', models.TextField(verbose_name='Текст новости')),
                ('image', models.ImageField(blank=True, null=True, upload_to='news/', verbose_name='Изображение')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('is_verified', models.BooleanField(default=True, verbose_name='Проверена администратором?')),
                ('categories', models.ManyToManyField(to='news_app.categorie', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]