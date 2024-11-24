from django.db import models

class Categorie(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Категория"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class New(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name='Заголовок'
    )
    author = models.CharField(
        max_length=100,
        verbose_name='Автор'
    )
    categories = models.ManyToManyField(
        Categorie,
        verbose_name='Категории'
    )
    description = models.TextField(
        max_length=500,
        verbose_name='Описание'
    )
    tetx = models.TextField(        
        verbose_name='Текст новости'
    )
    image = models.ImageField(
        upload_to='news/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )
    is_verified = models.BooleanField(
        default=True,
        verbose_name='Проверена администратором?'
    )


    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)

   
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"