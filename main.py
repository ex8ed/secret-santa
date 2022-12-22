# -*- coding: UTF-8 -*-
import pandas as pd
import config
import random
from collections import deque


class Generator:
    """Makes an output .txt file with pattern message"""

    def __init__(self, path='./data.xlsx'):
        """Constructor provides to work with a path to data table"""
        self._path = path
        self._pairs = {}

    def get_people_list(self):
        return self._pairs

    def __compare_people(self):
        """ Given a list of people, assign each one a secret santa partner
            from the list and return the pairings as a dict. Implemented to always
            create a perfect cycle """
        people_ = config.people
        random.shuffle(people_)
        partners = deque(people_)
        partners.rotate()
        self._pairs = dict(zip(people_, partners))

    def test_compare(self):
        self.__compare_people()
        print(self._pairs)

    def generate_message(self):
        data = pd.read_excel(self._path)
        with open('Messages.txt', 'w') as f:
            self.__compare_people()
            for guy in self._pairs.keys():
                gifted_name = self._pairs[guy]
                row_i = data.loc[data['ФИО'] == gifted_name].index[0]
                address = data.iloc[row_i]['Адрес парковки']
                index = data.iloc[row_i]['Индекс парковки']
                best_variant = data.iloc[row_i]['Самое лучшее за рулем тайного бусика?']
                especial_thing = data.iloc[row_i]['Без чего Новый год какой-то не новый?']
                decorations = data.iloc[row_i]['Как бы ты украсил свой тайный бусик?']
                best_gift = data.iloc[row_i]['Лучший подарок от тайного Хлеба?']
                film = data.iloc[row_i][
                    'Говорят в тайном бусике можно поставить телевизор. Какой фильм из 2022 ты бы посмотрел на новый год?']
                meal = data.iloc[row_i]['Бусику нравится 109 бензин, а какое твое любимое новогоднее блюдо?']
                people_count = data.iloc[row_i]['Сколько людей нужно, чтобы завести тайный бусик и уехать из смены?']
                print(gifted_name,
                      address,
                      index,
                      best_variant,
                      especial_thing,
                      decorations,
                      best_gift,
                      film,
                      meal,
                      people_count)
                f.write(f'Отправитель: {guy}\n')
                f.write('###########################################\n')
                f.write(config.default_message.format(gifted_name=gifted_name,
                                                      address=address,
                                                      index=index,
                                                      best_variant=best_variant,
                                                      especial_thing=especial_thing,
                                                      decorations=decorations,
                                                      best_gift=best_gift,
                                                      film=film,
                                                      meal=meal,
                                                      people_count=people_count))
                f.write('###########################################\n\n')


if __name__ == "__main__":
    generator = Generator()
    generator.generate_message()
