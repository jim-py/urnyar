from django.db import models


class Urna(models.Model):
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

    main_photo = models.ImageField(upload_to='media/urna/%Y-%m-%d/', blank=True, verbose_name='Главная фотография')
    photo_color1 = models.ImageField(upload_to='media/urna/%Y-%m-%d/', blank=True, verbose_name='Основной цвет')
    photo_color2 = models.ImageField(upload_to='media/urna/%Y-%m-%d/', blank=True, verbose_name='Второй цвет')
    photo_color3 = models.ImageField(upload_to='media/urna/%Y-%m-%d/', blank=True, verbose_name='Третий цвет')
    photo_color4 = models.ImageField(upload_to='media/urna/%Y-%m-%d/', blank=True, verbose_name='Четвёртый цвет')
    photo_color5 = models.ImageField(upload_to='media/urna/%Y-%m-%d/', blank=True, verbose_name='Пятый цвет')
    photo_color6 = models.ImageField(upload_to='media/urna/%Y-%m-%d/', blank=True, verbose_name='Шестой цвет')
    photo_color7 = models.ImageField(upload_to='media/urna/%Y-%m-%d/', blank=True, verbose_name='Седьмой цвет')
    photo_color8 = models.ImageField(upload_to='media/urna/%Y-%m-%d/', blank=True, verbose_name='Восьмой цвет')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урна'
        verbose_name_plural = 'Урны'


class UrnaMetal(models.Model):
    name = models.CharField(max_length=20, blank=True, verbose_name='Название')
    cost = models.CharField(max_length=20, blank=True, verbose_name='Стоимость')
    tip = models.ForeignKey('ItemTip', verbose_name='Тип', on_delete=models.CASCADE, blank=True)

    volume1_05 = models.CharField(max_length=20, blank=True, verbose_name='Первый объём')
    volume2_05 = models.CharField(max_length=20, blank=True, verbose_name='Второй объём')
    weight1_05 = models.CharField(max_length=20, blank=True, verbose_name='Первый вес')
    weight2_05 = models.CharField(max_length=20, blank=True, verbose_name='Второй вес')
    size1_05 = models.CharField(max_length=20, blank=True, verbose_name='Первый габарит')
    size2_05 = models.CharField(max_length=20, blank=True, verbose_name='Второй габарит')

    cost1_1_05 = models.CharField(max_length=20, blank=True, verbose_name='Первая стоимость от 1 шт.')
    cost1_2_05 = models.CharField(max_length=20, blank=True, verbose_name='Вторая стоимость от 1 шт.')
    cost50_1_05 = models.CharField(max_length=20, blank=True, verbose_name='Первая стоимость от 100 шт.')
    cost50_2_05 = models.CharField(max_length=20, blank=True, verbose_name='Вторая стоимость от 100 шт.')
    cost100_1_05 = models.CharField(max_length=20, blank=True, verbose_name='Первая стоимость от 200 шт.')
    cost100_2_05 = models.CharField(max_length=20, blank=True, verbose_name='Вторая стоимость от 200 шт.')

    volume1_07 = models.CharField(max_length=20, blank=True, verbose_name='Первый объём')
    volume2_07 = models.CharField(max_length=20, blank=True, verbose_name='Второй объём')
    volume3_07 = models.CharField(max_length=20, blank=True, verbose_name='Третий объём')
    weight1_07 = models.CharField(max_length=20, blank=True, verbose_name='Первый вес')
    weight2_07 = models.CharField(max_length=20, blank=True, verbose_name='Второй вес')
    weight3_07 = models.CharField(max_length=20, blank=True, verbose_name='Третий вес')
    size1_07 = models.CharField(max_length=20, blank=True, verbose_name='Первый габарит')
    size2_07 = models.CharField(max_length=20, blank=True, verbose_name='Второй габарит')
    size3_07 = models.CharField(max_length=20, blank=True, verbose_name='Третий габарит')

    cost1_1_07 = models.CharField(max_length=20, blank=True, verbose_name='Первая стоимость от 1 шт.')
    cost1_2_07 = models.CharField(max_length=20, blank=True, verbose_name='Вторая стоимость от 1 шт.')
    cost1_3_07 = models.CharField(max_length=20, blank=True, verbose_name='Третья стоимость от 1 шт.')
    cost50_1_07 = models.CharField(max_length=20, blank=True, verbose_name='Первая стоимость от 100 шт.')
    cost50_2_07 = models.CharField(max_length=20, blank=True, verbose_name='Вторая стоимость от 100 шт.')
    cost50_3_07 = models.CharField(max_length=20, blank=True, verbose_name='Третья стоимость от 100 шт.')
    cost100_1_07 = models.CharField(max_length=20, blank=True, verbose_name='Первая стоимость от 200 шт.')
    cost100_2_07 = models.CharField(max_length=20, blank=True, verbose_name='Вторая стоимость от 200 шт.')
    cost100_3_07 = models.CharField(max_length=20, blank=True, verbose_name='Третья стоимость от 200 шт.')

    material_text = models.CharField(max_length=500, blank=True, verbose_name='Описание материала')
    color_text = models.CharField(max_length=500, blank=True, verbose_name='Цвета')
    cover_text = models.CharField(max_length=500, blank=True, verbose_name='Покрытие')
    plug = models.CharField(max_length=500, blank=True, verbose_name='Наличие заглушек')
    box_type_text = models.CharField(max_length=500, blank=True, verbose_name='Тип упаковки')
    tray_text = models.CharField(max_length=500, blank=True, verbose_name='Наличие пепельницы')
    extra_text = models.CharField(max_length=500, blank=True, verbose_name='Дополнительное описание')

    main_photo = models.ImageField(upload_to=f'media/{name}/%Y-%m-%d/', blank=True, verbose_name='Главная фотография')
    photo_color1 = models.ImageField(upload_to='media/urna_metal/%Y-%m-%d/', blank=True, verbose_name='Основной цвет')
    photo_color2 = models.ImageField(upload_to='media/urna_metal/%Y-%m-%d/', blank=True, verbose_name='Второй цвет')
    photo_color3 = models.ImageField(upload_to='media/urna_metal/%Y-%m-%d/', blank=True, verbose_name='Третий цвет')
    photo_color4 = models.ImageField(upload_to='media/urna_metal/%Y-%m-%d/', blank=True, verbose_name='Четвёртый цвет')
    photo_color5 = models.ImageField(upload_to='media/urna_metal/%Y-%m-%d/', blank=True, verbose_name='Пятый цвет')
    photo_color6 = models.ImageField(upload_to='media/urna_metal/%Y-%m-%d/', blank=True, verbose_name='Шестой цвет')
    photo_color7 = models.ImageField(upload_to='media/urna_metal/%Y-%m-%d/', blank=True, verbose_name='Седьмой цвет')
    photo_color8 = models.ImageField(upload_to='media/urna_metal/%Y-%m-%d/', blank=True, verbose_name='Восьмой цвет')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урна металл'
        verbose_name_plural = 'Урны металл'


class Bench(models.Model):
    name = models.CharField(max_length=20, blank=True, verbose_name='Название')
    cost = models.CharField(max_length=20, blank=True, verbose_name='Стоимость')
    tip = models.ForeignKey('ItemTip', verbose_name='Тип', on_delete=models.CASCADE, blank=True)

    size1 = models.CharField(max_length=20, blank=True, verbose_name='Первый габарит')
    size2 = models.CharField(max_length=20, blank=True, verbose_name='Второй габарит')
    size3 = models.CharField(max_length=20, blank=True, verbose_name='Третий габарит')
    weight1 = models.CharField(max_length=20, blank=True, verbose_name='Первый вес')
    weight2 = models.CharField(max_length=20, blank=True, verbose_name='Второй вес')
    weight3 = models.CharField(max_length=20, blank=True, verbose_name='Третий вес')
    cost1 = models.CharField(max_length=20, blank=True, verbose_name='Стоимость от 1 шт.')
    cost50 = models.CharField(max_length=20, blank=True, verbose_name='Стоимость от 50 шт.')
    cost100 = models.CharField(max_length=20, blank=True, verbose_name='Стоимость от 100 шт.')

    text = models.CharField(max_length=500, blank=True, verbose_name='Описание лавочки')
    material_text = models.CharField(max_length=500, blank=True, verbose_name='Материал')
    size_text = models.CharField(max_length=500, blank=True, verbose_name='Габаритные размеры')
    weight_text = models.CharField(max_length=500, blank=True, verbose_name='Вес')
    size_timber_text = models.CharField(max_length=500, blank=True, verbose_name='Размер бруса')

    main_photo = models.ImageField(upload_to='media/bench/%Y-%m-%d/', blank=True, verbose_name='Главная фотография')
    photo_color1 = models.ImageField(upload_to='media/bench/%Y-%m-%d/', blank=True, verbose_name='Основной цвет')
    photo_color2 = models.ImageField(upload_to='media/bench/%Y-%m-%d/', blank=True, verbose_name='Второй цвет')
    photo_color3 = models.ImageField(upload_to='media/bench//%Y-%m-%d/', blank=True, verbose_name='Третий цвет')
    photo_color4 = models.ImageField(upload_to='media/bench/%Y-%m-%d/', blank=True, verbose_name='Четвёртый цвет')
    photo_color5 = models.ImageField(upload_to='media/bench/%Y-%m-%d/', blank=True, verbose_name='Пятый цвет')
    photo_color6 = models.ImageField(upload_to='media/bench/%Y-%m-%d/', blank=True, verbose_name='Шестой цвет')
    photo_color7 = models.ImageField(upload_to='media/bench/%Y-%m-%d/', blank=True, verbose_name='Седьмой цвет')
    photo_color8 = models.ImageField(upload_to='media/bench/%Y-%m-%d/', blank=True, verbose_name='Восьмой цвет')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лавка'
        verbose_name_plural = 'Лавки'


class Bases(models.Model):
    name = models.CharField(max_length=20, blank=True, verbose_name='Название')
    cost = models.CharField(max_length=20, blank=True, verbose_name='Стоимость')
    tip = models.ForeignKey('ItemTip', verbose_name='Тип', on_delete=models.CASCADE, blank=True)

    volume1 = models.CharField(max_length=20, blank=True, verbose_name='Первый объём')
    volume2 = models.CharField(max_length=20, blank=True, verbose_name='Второй объём')
    volume3 = models.CharField(max_length=20, blank=True, verbose_name='Третий объём')
    size1 = models.CharField(max_length=20, blank=True, verbose_name='Первый габарит')
    size2 = models.CharField(max_length=20, blank=True, verbose_name='Второй габарит')
    size3 = models.CharField(max_length=20, blank=True, verbose_name='Третий габарит')
    weight1 = models.CharField(max_length=20, blank=True, verbose_name='Первый вес')
    weight2 = models.CharField(max_length=20, blank=True, verbose_name='Второй вес')
    weight3 = models.CharField(max_length=20, blank=True, verbose_name='Третий вес')
    cost1 = models.CharField(max_length=20, blank=True, verbose_name='Стоимость от 1 шт.')
    cost10 = models.CharField(max_length=20, blank=True, verbose_name='Стоимость от 10 шт.')
    cost50 = models.CharField(max_length=20, blank=True, verbose_name='Стоимость от 50 шт.')

    country = models.CharField(max_length=500, blank=True, verbose_name='Страна бренда')
    height_base = models.CharField(max_length=500, blank=True, verbose_name='Высота основания')
    material = models.CharField(max_length=500, blank=True, verbose_name='Материал ламелей')
    tip_lamel = models.CharField(max_length=500, blank=True, verbose_name='Тип ламелей')
    supp = models.CharField(max_length=500, blank=True, verbose_name='Опора')
    distance = models.CharField(max_length=500, blank=True, verbose_name='Расстояние между ламелиями')
    max_weight = models.CharField(max_length=500, blank=True, verbose_name='Максимальный вес на 1 спальное место')
    color = models.CharField(max_length=500, blank=True, verbose_name='Цвет каркаса')
    safe = models.CharField(max_length=500, blank=True, verbose_name='Гарантия')
    tip_base = models.CharField(max_length=500, blank=True, verbose_name='Тип основания')
    height_legs = models.CharField(max_length=500, blank=True, verbose_name='Высота ножек')

    main_photo = models.ImageField(upload_to='media/bases/%Y-%m-%d/', blank=True, verbose_name='Главная фотография')
    photo_color1 = models.ImageField(upload_to='media/bases/%Y-%m-%d/', blank=True, verbose_name='Основной цвет')
    photo_color2 = models.ImageField(upload_to='media/bases/%Y-%m-%d/', blank=True, verbose_name='Второй цвет')
    photo_color3 = models.ImageField(upload_to='media/bases//%Y-%m-%d/', blank=True, verbose_name='Третий цвет')
    photo_color4 = models.ImageField(upload_to='media/bases/%Y-%m-%d/', blank=True, verbose_name='Четвёртый цвет')
    photo_color5 = models.ImageField(upload_to='media/bases/%Y-%m-%d/', blank=True, verbose_name='Пятый цвет')
    photo_color6 = models.ImageField(upload_to='media/bases/%Y-%m-%d/', blank=True, verbose_name='Шестой цвет')
    photo_color7 = models.ImageField(upload_to='media/bases/%Y-%m-%d/', blank=True, verbose_name='Седьмой цвет')
    photo_color8 = models.ImageField(upload_to='media/bases/%Y-%m-%d/', blank=True, verbose_name='Восьмой цвет')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Основание'
        verbose_name_plural = 'Основания'


class ItemTip(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название типа', blank=True)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE, blank=True)
    photo = models.ImageField(upload_to='media/%Y-%m-%d/', blank=True, verbose_name='Фото категории')

    class Meta:
        verbose_name = 'Тип предмета'
        verbose_name_plural = 'Типы предмета'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории', blank=True)

    class Meta:
        verbose_name = 'Категория типа'
        verbose_name_plural = 'Категории типа'

    def __str__(self):
        return self.name
