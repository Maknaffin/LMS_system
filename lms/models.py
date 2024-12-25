from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name='название урока')
    image = models.ImageField(verbose_name='картинка урока', **NULLABLE)
    description = models.TextField(verbose_name='описание урока', **NULLABLE)
    link_to_video = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              verbose_name='пользователь', **NULLABLE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='lesson',
                               verbose_name='курс', **NULLABLE)

    def __str__(self):
        return f'{self.title} - {self.description}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='название курса')
    image = models.ImageField(verbose_name='картинка курса', **NULLABLE)
    description = models.TextField(verbose_name='описание курса', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.title} - {self.description}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
