"""Документация модуля. Описывает работу классов и функций.
Размещается в верхней части файла (начиная с первой строки).
"""
# # Импортируйте модуль inspect.
# import inspect


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

from math import sqrt


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> str:
    """Выводит значение квадратного корня из заданного числа > 0 или 0.0."""
    if your_number <= 0:
        return '0.0'
    root = calculate_square_root(your_number)
    return (f'Мы вычислили квадратный корень из введённого вами числа. '
            f'Это будет: {root}')


print('Добро пожаловать в самую лучшую программу для вычисления '
      'квадратного корня из заданного числа')
result = calc(25.5)
print(result)


quit()

# Тестовые данные.
TEST_DATA: list[tuple[int, str, bool]] = [
    (44, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]

BONUS: float = 1.1
ANTIBONUS: float = 0.8


def add_rep(current_rep: float, rep_points: int, buf_effect: bool) -> float:
    current_rep += rep_points
    if buf_effect:
        return current_rep * BONUS
    return current_rep


def remove_rep(current_rep: float,
               rep_points: int,
               debuf_effect: bool) -> float:
    current_rep -= rep_points
    if debuf_effect:
        return current_rep * ANTIBONUS
    return current_rep


def main(duel_res: list[tuple[int, str, bool]]) -> str:
    current_rep: float = 0.0
    for rep, result, effect in duel_res:
        if result == 'success':
            current_rep = add_rep(current_rep, rep, effect)
        if result == 'failure':
            current_rep = remove_rep(current_rep, rep, effect)
    return (f'После {len(duel_res)} поединков, репутация персонажа — '
            f'{current_rep:.3f} очков.')


# Тестовый вызов функции main.
print(main(TEST_DATA))
