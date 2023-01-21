from random import randint
from graphic_arts.start_game_banner import run_screensaver

# String literals for 79-longer lines 
DAMAGE_LINE: str = 'нанёс урон противнику, равный'
SPEC_SKILL_LINE: str = 'применил специальное умение'
ENTER_CMDS_LINE: str = ''.join([
    'Введи одну из команд: attack — чтобы атаковать противника, ',
    'defence — чтобы блокировать атаку противника или special — чтобы',
    ' использовать свою суперсилу.'
])
ENTER_HERO_NAME_LINE: str = ''.join([
    'Введи название персонажа, за которого хочешь играть: Воитель — warrior, ',
    'Маг — mage, Лекарь — healer: '
])
WARRIOR_LINE: str = ''.join(['Воитель — дерзкий воин ближнего боя. Сильный, ',
                             'выносливый и отважный.'])
MAGE_LINE: str = ''.join(['Маг — находчивый воин дальнего боя. Обладает ',
                          'высоким интеллектом.'])
HEALER_LINE: str = ''.join(['Лекарь — могущественный заклинатель. Черпает ',
                            'силы из природы, веры и духов.'])
APPR_CHOICE_LINE: str = ''.join([
    'Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, чтобы ',
    'выбрать другого персонажа '
])


def attack(char_name: str, char_class: str) -> str:
    """Attack per hero.
    Args: hero name, hero class.
    Return: a str representation of damage the hero can do."""

    res: str = ''
    if char_class == 'warrior':
        res = f'{char_name} {DAMAGE_LINE} {5 + randint(3, 5)}'
    if char_class == 'mage':
        res = f'{char_name} {DAMAGE_LINE} {5 + randint(5, 10)}'
    if char_class == 'healer':
        res = f'{char_name} {DAMAGE_LINE} {5 + randint(-3, -1)}'
    return res


def defence(char_name: str, char_class: str) -> str:
    """Defense per hero.
    Args: hero name, hero class.
    Return: a str representation of defence the hero is capable of."""

    res: str = ''
    if char_class == 'warrior':
        res = f'{char_name} блокировал {10 + randint(5, 10)} урона'
    if char_class == 'mage':
        res = f'{char_name} блокировал {10 + randint(-2, 2)} урона'
    if char_class == 'healer':
        res = f'{char_name} блокировал {10 + randint(2, 5)} урона'
    return res


def special(char_name: str, char_class: str) -> str:
    """Special skill per hero.
    Args: hero name, hero class.
    Return: a str representation of magic the hero can cast."""

    res: str = ''
    if char_class == 'warrior':
        res = f'{char_name} {SPEC_SKILL_LINE} «Выносливость {80 + 25}»'
    if char_class == 'mage':
        res = f'{char_name} {SPEC_SKILL_LINE} «Атака {5 + 40}»'
    if char_class == 'healer':
        res = f'{char_name} {SPEC_SKILL_LINE} «Защита {10 + 30}»'
    return res


def start_training(char_name: str, char_class: str) -> str:
    """Start training as per hero.
    Args: hero name, hero class.
    Return: a str representation of attack/defence/special actions
    performed."""

    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print(ENTER_CMDS_LINE)
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Let the user choose their hero: warrior/mage/healer.
    Args: None.
    Return: a str representation of hero class."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input(ENTER_HERO_NAME_LINE)
        if char_class == 'warrior':
            print(WARRIOR_LINE)
        if char_class == 'mage':
            print(MAGE_LINE)
        if char_class == 'healer':
            print(HEALER_LINE)
        approve_choice = input(APPR_CHOICE_LINE).lower()
    return char_class


if __name__ == '__main__':
    """Start the app, run the screensaver, start the game on pressing 'X',
    introduce the user and save their choice of hero:
    warrior/mage/healer, and then offer to start training.
    Args: None.
    Return: None."""

    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    start_training(char_name, char_class)
