from django.db import models
from django.utils import timezone

from .makedir import makedir

class Person(models.Model):

    STATUS_CHOICES = (
        (0, 'Готов к созданию отчета!'),
        (1, 'Собираю информацию!'),
        (2, 'Необходимо разметить материал!'),
        (3 , 'Скачать таблицу!'),
    )

    start_table = models.FileField(verbose_name='Стартовый шаблон')
    created_at = models.DateField(default=timezone.now, verbose_name='Дата создания')
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    start_date = models.DateField(default=timezone.now, verbose_name='Дата начала проекта')
    end_date = models.DateField(default=timezone.now, verbose_name='Дата окончания')
    last_it = models.IntegerField(default=0, verbose_name='Последняя итерация')
    status = models.IntegerField(verbose_name='Статус', default=0, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    @property
    def get_status(self):
        if self.status == 0:
            return 'Готов к созданию отчета!'
        elif self.status == 1:
            return 'Собираю информацию!'
        elif self.status == 2:
            return 'Необходимо разметить материал!'
        elif self.status == 3:
            return 'Происходит создание таблицы!'
        return 'Отчет готов!'

    @property
    def get_screenshots_path(self):
        return f'Person_{self.id}/{self.last_it}/screenshots'

    @property
    def get_tables_path(self):
        return f'Person_{self.id}/{self.last_it}/tables'

    def mkdir(self):
        makedir(f'Person_{self.id}')
        makedir(f'Person_{self.id}/{self.last_it}')
        makedir(self.get_tables_path)
        makedir(self.get_screenshots_path)

    def mkit(self):
        self.last_it += 1
        self.status = 0
        self.save()

class Query(models.Model):
    query = models.CharField(max_length=200, verbose_name='Запрос')
    yandex_header = models.ImageField(blank=True, null=True)
    google_header = models.ImageField(blank=True, null=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Персона')

    def __str__(self):
        return self.query


class Url_data(models.Model):
    POSITIVE = 0
    NEGATIVE = 1
    UNKNOWN = -1
    TONE_CHOICES = (
        (POSITIVE, 'позитив'),
        (NEGATIVE, 'негатив'),
        (UNKNOWN, 'не размечено')
    )
    tone = models.IntegerField(choices=TONE_CHOICES, default=UNKNOWN, verbose_name='Тональность')
    href = models.CharField(max_length=400, verbose_name='Ссылка', unique=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Персона')

    def __str__(self):
        return self.href


class Url(models.Model):
    POSITIVE = 0
    NEGATIVE = 1
    TONE_CHOICES = (
        (POSITIVE, 'позитив'),
        (NEGATIVE, 'негатив'),
    )
    href = models.CharField(max_length=400, verbose_name='Ссылка')
    url_data = models.ForeignKey('Url_data', on_delete=models.CASCADE, verbose_name='Ссылка в базе')
    query = models.ForeignKey('Query', on_delete=models.CASCADE, verbose_name='Запрос')
    search_system = models.CharField(max_length=200, verbose_name='Поисковая система')
    image = models.ImageField(default='1_yandex_header.png', verbose_name='Картинка')
    position = models.IntegerField(default=0, verbose_name='Позиция')
    page_number = models.IntegerField(default=0, verbose_name='Номер страницы')
    page_position = models.IntegerField(default=0, verbose_name='Номер ссылки в странице')
    last_it = models.IntegerField(default=0, verbose_name='Последняя итерация')

    def __str__(self):
        return self.href


class Report(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Персона')
    table = models.CharField(max_length=400, verbose_name='Таблица отчета')
    letter = models.CharField(max_length=400, verbose_name='Сопроводительное письмо')
    table_name = models.CharField(max_length=200, verbose_name='Имя таблицы')
    letter_name = models.CharField(max_length=200, verbose_name='Название письма')
    created_at = models.DateField(default=timezone.now, verbose_name='Дата создания')
    last_it = models.IntegerField(default=0, verbose_name='Последняя итерация')

    def __str__(self):
        return self.table_name


class Exception(models.Model):
    tone = models.CharField(max_length=200, verbose_name='Тональность')
    href = models.CharField(max_length=400, verbose_name='Ссылка')
    person = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Персона')

    def __str__(self):
        return self.href
# Create your models here.
