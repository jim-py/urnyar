from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=20, blank=True, verbose_name='Название')
    cost = models.CharField(max_length=20, blank=True, verbose_name='Стоимость')
    tip = models.ForeignKey('ItemTip', verbose_name='Тип', on_delete=models.CASCADE, blank=True)

    volume1 = models.CharField(max_length=20, blank=True, verbose_name='Первый объём')
    volume2 = models.CharField(max_length=20, blank=True, verbose_name='Второй объём')
    volume3 = models.CharField(max_length=20, blank=True, verbose_name='Третий объём')
    material1 = models.CharField(max_length=20, blank=True, verbose_name='Первый металл')
    material2 = models.CharField(max_length=20, blank=True, verbose_name='Второй металл')
    material3 = models.CharField(max_length=20, blank=True, verbose_name='Третий металл')
    size1 = models.CharField(max_length=20, blank=True, verbose_name='Первый габарит')
    size2 = models.CharField(max_length=20, blank=True, verbose_name='Второй габарит')
    size3 = models.CharField(max_length=20, blank=True, verbose_name='Третий габарит')
    weight1 = models.CharField(max_length=20, blank=True, verbose_name='Первый вес')
    weight2 = models.CharField(max_length=20, blank=True, verbose_name='Второй вес')
    weight3 = models.CharField(max_length=20, blank=True, verbose_name='Третий вес')
    box1 = models.CharField(max_length=20, blank=True, verbose_name='Первая коробка')
    box2 = models.CharField(max_length=20, blank=True, verbose_name='Вторая коробка')
    box3 = models.CharField(max_length=20, blank=True, verbose_name='Третья коробка')

    cost1_1 = models.CharField(max_length=20, blank=True, verbose_name='Первая стоимость от 1 шт.')
    cost1_2 = models.CharField(max_length=20, blank=True, verbose_name='Вторая стоимость от 1 шт.')
    cost1_3 = models.CharField(max_length=20, blank=True, verbose_name='Третья стоимость от 1 шт.')
    cost100_1 = models.CharField(max_length=20, blank=True, verbose_name='Первая стоимость от 100 шт.')
    cost100_2 = models.CharField(max_length=20, blank=True, verbose_name='Вторая стоимость от 100 шт.')
    cost100_3 = models.CharField(max_length=20, blank=True, verbose_name='Третья стоимость от 100 шт.')
    cost200_1 = models.CharField(max_length=20, blank=True, verbose_name='Первая стоимость от 200 шт.')
    cost200_2 = models.CharField(max_length=20, blank=True, verbose_name='Вторая стоимость от 200 шт.')
    cost200_3 = models.CharField(max_length=20, blank=True, verbose_name='Третья стоимость от 200 шт.')

    material_text = models.CharField(max_length=500, blank=True, verbose_name='Описание материала')
    color_text = models.CharField(max_length=500, blank=True, verbose_name='Цвета')
    cover_text = models.CharField(max_length=500, blank=True, verbose_name='Покрытие')
    box_type_text = models.CharField(max_length=500, blank=True, verbose_name='Тип упаковки')
    tray_text = models.CharField(max_length=500, blank=True, verbose_name='Наличие пепельницы')
    extra_text = models.CharField(max_length=500, blank=True, verbose_name='Дополнительное описание')

    main_photo = models.ImageField(upload_to='media/%Y-%m-%d/', blank=True, verbose_name='Главная фотография')
    photo_color1 = models.ImageField(upload_to='media/%Y-%m-%d/', blank=True, verbose_name='Основной цвет')
    photo_color2 = models.ImageField(upload_to='media/%Y-%m-%d/', blank=True, verbose_name='Второй цвет')
    photo_color3 = models.ImageField(upload_to='media/%Y-%m-%d/', blank=True, verbose_name='Третий цвет')
    photo_color4 = models.ImageField(upload_to='media/%Y-%m-%d/', blank=True, verbose_name='Четвёртый цвет')
    photo_color5 = models.ImageField(upload_to='media/%Y-%m-%d/', blank=True, verbose_name='Пятый цвет')
    photo_color6 = models.ImageField(upload_to='media/%Y-%m-%d/', blank=True, verbose_name='Шестой цвет')
    photo_color7 = models.ImageField(upload_to='media/%Y-%m-%d/', blank=True, verbose_name='Седьмой цвет')
    photo_color8 = models.ImageField(upload_to='media/%Y-%m-%d/', blank=True, verbose_name='Восьмой цвет')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class ItemTip(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название типа', blank=True)
    photo = models.ImageField(upload_to='media/%Y-%m-%d/', blank=True, verbose_name='Фото категории')

    class Meta:
        verbose_name = 'Тип предмета'
        verbose_name_plural = 'Типы предметов'

    def __str__(self):
        return self.name
