import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urna.settings')
django.setup()

from main.models import *
from faker import Faker

fake = Faker('ru-RU')

tip = ItemTip.objects.values_list('id', flat=True).distinct()

for _ in range(100):
    Item.objects.create(name=fake.sentence(nb_words=1),
                        cost=random.randint(2000, 5000),
                        tip=fake.random_element(ItemTip.objects.filter(id=fake.random_element(tip))),

                        volume1=random.randint(2000, 5000),
                        volume2=random.randint(2000, 5000),
                        volume3=random.randint(2000, 5000),
                        material1=fake.sentence(nb_words=1),
                        material2=fake.sentence(nb_words=1),
                        material3=fake.sentence(nb_words=1),
                        size1=random.randint(2000, 5000),
                        size2=random.randint(2000, 5000),
                        size3=random.randint(2000, 5000),
                        weight1=random.randint(2000, 5000),
                        weight2=random.randint(2000, 5000),
                        weight3=random.randint(2000, 5000),
                        box1=fake.sentence(nb_words=1),
                        box2=fake.sentence(nb_words=1),
                        box3=fake.sentence(nb_words=1),

                        cost1_1=random.randint(2000, 5000),
                        cost1_2=random.randint(2000, 5000),
                        cost1_3=random.randint(2000, 5000),
                        cost100_1=random.randint(2000, 5000),
                        cost100_2=random.randint(2000, 5000),
                        cost100_3=random.randint(2000, 5000),
                        cost200_1=random.randint(2000, 5000),
                        cost200_2=random.randint(2000, 5000),
                        cost200_3=random.randint(2000, 5000),

                        material_text=fake.sentence(nb_words=10),
                        color_text=fake.sentence(nb_words=10),
                        cover_text=fake.sentence(nb_words=10),
                        box_type_text=fake.sentence(nb_words=10),
                        tray_text=fake.sentence(nb_words=10),
                        extra_text=fake.sentence(nb_words=10),

                        main_photo='media/2022-11-02/360_urna-tallin.jpeg',
                        photo_color1='media/2022-11-02/360_urna-tallin.jpeg',)

for _ in range(0):
    ItemTip.objects.create(name=fake.sentence(nb_words=1),)
