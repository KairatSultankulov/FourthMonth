from django.db import models

class Films(models.Model):
    GENRE = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
    )
    image = models.ImageField(upload_to='films/', verbose_name='загрузите фото', null=True)
    title = models.CharField(max_length=100, verbose_name='укажите название', null=True)
    description = models.TextField(verbose_name='укажите описание фильма', null=True, blank=True)
    price = models.FloatField(verbose_name='укажите цену', null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='укажите дату выхода', null=True)
    genre = models.CharField(max_length=10, choices=GENRE, verbose_name='укажите жанр', null=True)
    time = models.TimeField(verbose_name='укажите время', null=True)
    director = models.CharField(max_length=100, verbose_name='укажите режисера', null=True)
    trailer = models.URLField(null=True, verbose_name='вставьте ссылку на трейлер',)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural ='фильмы'

class Reviews(models.Model):
    GRADE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    choice_film = models.ForeignKey(Films, on_delete=models.CASCADE,
                                    related_name='reviews', verbose_name='выберите фильм', null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='укажите дату выхода', null=True)
    description = models.TextField(verbose_name='укажите описание фильма', null=True, blank=True)
    grade  = models.CharField(max_length=10, choices=GRADE,default='1', verbose_name='Поставьте оценку', null=True)
    def __str__(self):
        return f'{self.choice_film.title} - {self.grade}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'