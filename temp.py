class Bird:
    """Create a bird instance."""

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False) -> str:
        """Return a bird's description: its name, size."""
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    """Create a Parrot instance based on the Bird class, with a color
    property too."""

    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color

    def describe(self, full=None) -> str:
        if full:
            return (f'Попугай {self.name} — заметная птица, окрас её перьев — '
                    f'{self.color}, а размер — {self.size}. Интересный факт: '
                    f'попугаи чувствуют ритм, а вовсе не бездумно двигаются '
                    f'под музыку. Если сменить композицию, то и темп движений '
                    f'птицы изменится.')
        return super().describe()


class Penguin(Bird):
    """Create a Penguin instance based on the Bird class, with a genus
    property of their own."""

    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus

    def describe(self, full=None) -> str:
        if full:
            return (f'Размер пингвина {self.name} из рода {self.genus} — '
                    f'{self.size}. Интересный факт: однажды группа '
                    f'геологов-разведчиков похитила пингвинье яйцо, и их '
                    f'принялась преследовать вся стая, не пытаясь, впрочем, '
                    f'при этом нападать. Посовещавшись, похитители вернули '
                    f'птицам яйцо, и те отстали.')
        return super().describe()


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')
# Вызов метода у созданных объектов.
print(kesha.describe())
print(kowalski.describe(True))


# Вызов метода у созданных объектов.
# kesha.describe()
# kowalski.describe(True)


# # Импортируйте модуль inspect.
# import inspect
# import time
# from datetime import datetime as dt


# class Quest:
#     """Docstring for Quest"""

#     def __init__(self, name, description, goal):
#         self.name = name
#         self.description = description
#         self.goal = goal
#         self.start_time = self.end_time = None

#     def accept_quest(self) -> str:
#         if self.end_time is not None:
#             return 'С этим испытанием вы уже справились.'
#         self.start_time = dt.now()
#         return f'Начало "{self.name}" положено.'

#     def pass_quest(self) -> str:
#         if self.start_time is None:
#             return 'Нельзя завершить то, что не имеет начала!'
#         self.end_time = dt.now()
#         completion_time = self.end_time - self.start_time
#         return (f'Квест "{self.name}"" окончен. Время выполнения квеста: '
#                 f'{completion_time}.')

#     def __str__(self):
#         if self.end_time is not None and self.start_time is not None:
#             adder = 'Квест завершён.'
#         else:
#             adder = 'Квест выполняется.'
#         return f'Цель квеста "{self.name}" — {self.goal} {adder}'


# quest_name = 'Сбор пиксельники'
# quest_goal = 'Соберите 12 ягод пиксельники.'
# quest_description = '''
# В древнем лесу Кодоборье растёт ягода "пиксельника".
# Она нужна для приготовления целебных снадобий.
# Соберите 12 ягод пиксельники.'''

# new_quest = Quest(quest_name, quest_description, quest_goal)

# print(new_quest.pass_quest())
# print(new_quest.accept_quest())
# time.sleep(3)
# print(new_quest.pass_quest())
# print(new_quest.accept_quest())

# # Печатаем объекта класса Quest:
# print(new_quest)


# def tricky_func(self):
#     """Описывает работу функции tricky_func."""
#     ...


# class Test:
#     """Класс Test используется для демонстрации docstring."""

#     def first(self) -> str:
#         """Описывает метод first и демонстрирует перенос строки
#         документации.
#         """
#         return ''


# print('Без применения cleandoc:')
# print(Test.first.__doc__)
# print('С применением cleandoc:')
# # Выведите докстринг, используя метод cleandoc().
# print(inspect.cleandoc(Test.first.__doc__))

# from math import sqrt


# def calculate_square_root(number: float) -> float:
#     """Вычисляет квадратный корень."""
#     return sqrt(number)


# def calc(your_number: float) -> str:
#     """Выводит значение квадратного корня из заданного числа > 0 или 0.0."""
#     if your_number <= 0:
#         return '0.0'
#     root = calculate_square_root(your_number)
#     return (f'Мы вычислили квадратный корень из введённого вами числа. '
#             f'Это будет: {root}')


# print('Добро пожаловать в самую лучшую программу для вычисления '
#       'квадратного корня из заданного числа')
# result = calc(25.5)
# print(result)


# quit()

# # Тестовые данные.
# TEST_DATA: list[tuple[int, str, bool]] = [
#     (44, 'success', True),
#     (16, 'failure', True),
#     (4, 'success', False),
#     (21, 'failure', False),
# ]

# BONUS: float = 1.1
# ANTIBONUS: float = 0.8


# def add_rep(current_rep: float, rep_points: int, buf_effect: bool) -> float:
#     current_rep += rep_points
#     if buf_effect:
#         return current_rep * BONUS
#     return current_rep


# def remove_rep(current_rep: float,
#                rep_points: int,
#                debuf_effect: bool) -> float:
#     current_rep -= rep_points
#     if debuf_effect:
#         return current_rep * ANTIBONUS
#     return current_rep


# def main(duel_res: list[tuple[int, str, bool]]) -> str:
#     current_rep: float = 0.0
#     for rep, result, effect in duel_res:
#         if result == 'success':
#             current_rep = add_rep(current_rep, rep, effect)
#         if result == 'failure':
#             current_rep = remove_rep(current_rep, rep, effect)
#     return (f'После {len(duel_res)} поединков, репутация персонажа — '
#             f'{current_rep:.3f} очков.')


# # Тестовый вызов функции main.
# print(main(TEST_DATA))
