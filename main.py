from random import randint


DAMAGE_LINE = "нанёс урон противнику, равный"
SPEC_SKILL_LINE = "применил специальное умение"


ENTER_CMDS_LINE = ''.join([
    'Введи одну из команд: attack — чтобы атаковать противника, ',
    'defence — чтобы блокировать атаку противника или special — чтобы',
    'использовать свою суперсилу.'
])


ENTER_HERO_NAME_LINE = ''.join([
    'Введи название персонажа, за которого хочешь играть: Воитель — warrior, ',
    'Маг — mage, Лекарь — healer: '
])
WARRIOR_LINE = ''.join(['Воитель — дерзкий воин ближнего боя. Сильный, ',
                        'выносливый и отважный.'])
MAGE_LINE = ''.join(['Маг — находчивый воин дальнего боя. Обладает высоким ',
                     'интеллектом.'])
HEALER_LINE = ''.join(['Лекарь — могущественный заклинатель. Черпает силы из ',
                       'природы, веры и духов.'])
APPR_CHOICE_LINE = ''.join([
    'Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, чтобы ',
    'выбрать другого персонажа '
])


def attack(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} {DAMAGE_LINE} {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} {DAMAGE_LINE} {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} {DAMAGE_LINE} {5 + randint(-3, -1)}')


def defence(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')


def special(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} {SPEC_SKILL_LINE} «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} {SPEC_SKILL_LINE} «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} {SPEC_SKILL_LINE} «Защита {10 + 30}»')


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print(ENTER_CMDS_LINE)
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input(ENTER_HERO_NAME_LINE)
        if char_class == 'warrior':
            print(WARRIOR_LINE)
        if char_class == 'mage':
            print()
        if char_class == 'healer':
            print(HEALER_LINE)
        approve_choice = input(APPR_CHOICE_LINE).lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


if __name__ == '__main__':
    main()
