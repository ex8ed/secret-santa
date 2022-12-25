# -*- coding: UTF-8 -*-
import pandas as pd
import config
import random
import codecs
from collections import deque


class Generator:
    """Makes an output .txt file with pattern message"""

    def __init__(self, path='./data.xlsx'):
        """Constructor provides to work with a path to data table"""
        self._path = path
        self._pairs = {}
        self._people = []

    # a pack of getters for protected members
    def get_pairs(self):
        return self._pairs

    def get_people(self):
        return self._people

    def __get_people_from_doc(self):
        """Getting people from the list in the document"""
        data = pd.read_excel('./data.xlsx')
        self._people = list(data['ФИО'])

    def __compare_people(self):
        """ Given a list of people, assign each one a secret santa partner
            from the list and return the pairings as a dict. Implemented to always
            create a perfect cycle """
        self.__get_people_from_doc()
        random.shuffle(self._people)
        partners = deque(self._people)
        partners.rotate()
        self._pairs = dict(zip(self._people, partners))

    def test_compare(self):
        self.__compare_people()
        self.get_pairs()

    def generate_message(self):
        """Generates messages to a text-file in the current directory"""
        data = pd.read_excel(self._path)
        with codecs.open('messages.txt', 'w', "utf_8_sig") as f:
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
                f.write(f'Отправитель: {guy}, --> {gifted_name}\n')
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
