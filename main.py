"""
The same character creation module, yet with classes, to carry on.
"""
from random import randint
from graphic_arts.start_game_banner import run_screensaver


# Global string literals
DEFAULT_ATTACK: int = 5
DEFAULT_DEFENCE: int = 10
DEFAULT_STAMINA: int = 80

BLOCK_LINE: str = 'блокировал'
DAMAGE_UNIT: str = 'ед. урона'
DAMAGE_LINE: str = 'нанёс урон противнику, равный'
SPEC_SKILL_LINE: str = 'применил специальное умение'

# ENTER_CMDS_LINE: str = ''.join(
#     ['Введи одну из команд: attack — чтобы атаковать противника, ',
#      'defence — чтобы блокировать атаку противника или special — чтобы',
#      ' использовать свою суперсилу.',
#      ])
# ENTER_HERO_NAME_LINE: str = ''.join(
#   ['Введи название персонажа, за которого хочешь играть: Воитель — warrior,',
#      ' Маг — mage, Лекарь — healer: ',
#      ])

# MAGE_LINE: str = ''.join(['Маг — находчивый воин дальнего боя. Обладает ',
#                           'высоким интеллектом.'])
# HEALER_LINE: str = ''.join(['Лекарь — могущественный заклинатель. Черпает ',
#                              'силы из природы, веры и духов.'])
# APPR_CHOICE_LINE: str = ''.join(
#     ['Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, чтобы ',
#      'выбрать другого персонажа ',
#      ])


class Character:
    """Create a character basic for others to inherit from."""

    # Basic class constants.
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_BUFF = 15
    SPECIAL_SKILL = 'Удача'

    def __init__(self, name):
        self.name = name

    def attack(self):
        """Attack to be later overridden per character.
        Args: character name, character class.
        Return: a str representation of damage a character can do.
        """
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} {DAMAGE_LINE} {value_attack}'

    def defence(self):
        """Defence per character.
        Args: character name, character class.
        Return: a str representation of defence a character is capable of
        as per their class."""
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} {BLOCK_LINE} {value_defence} {DAMAGE_UNIT}.')

    def special(self):
        """Use a special skill per character.
        Args: character name, character class.
        Return: a str representation of magic a character can cast.
        """
        return (f'{self.name} {SPEC_SKILL_LINE} '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        """Describe a character based on their class."""
        return f'{self.__class__.__name__} — {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    """Create a Warrior instance of the Character class."""
    BRIEF_DESC_CHAR_CLASS: str = ('дерзкий воин ближнего боя. '
                                  'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    """Create a Mage instance of the Character class."""
    BRIEF_DESC_CHAR_CLASS = ('находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    """Create a Healer instance of the Character class."""
    BRIEF_DESC_CHAR_CLASS = ('могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def choice_char_class(char_name: str) -> Character:
    """Choose your Character: warrior/mage/healer.
    Args: a name string.
    Return: an instance of the chosen class.
    """
    # Add a helper dictionary.
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

    approve_choice: str = ''

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        try:
            char_class: Character = game_classes[selected_class](char_name)
        except KeyError:
            print('Такого персонажа пока нет. По умолчанию выбран '
                  'Маг. Или выбери другой из имеющихся.')
            char_class: Character = Mage(char_name)  # type: ignore[no-redef]

        # Вывели в терминал описание персонажа.
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(character):
    """Start training as per your Character instance.
    Args: the chosen character name and character class.
    Return: a str representation of the training loop actions
    performed.
    """

    # # Замените конструкцию условных операторов на словарь.
    # desc_per_class: dict[str, str] = {  # type: ignore[annotation-unchecked]
    #     'Warrior': (
    #         f'{character.name}, ты Воитель — великий мастер ближнего боя.'
    #     ),
    #   'Mage': f'{character.name}, ты Маг — превосходный укротитель стихий.',
    #     'Healer': (
    #       f'{character.name}, ты  Лекарь — чародей, способный исцелять раны.'
    #     ),
    # }
    # print(desc_per_class[character.__class__.__name__])

    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')

    # Команды для тренировки можно вынести в словарь
    # commands, где ключами будут строковые команды от пользователя, а
    # значениями — методы объекта, который принимает функция. Блок, который
    # отвечает за вывод описания персонажа, совсем уберите из кода проекта.
    # Доработайте код самостоятельно.

    commands: dict[str, str] = {  # type: ignore[annotation-unchecked]
        'attack': character.attack(),
        'defence': character.defence(),
        'special': character.special(),
        'skip': 'Тренировка окончена.',
    }

    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        # Вместо блока условных операторов добавьте условие
        # принадлежности введённой команды словарю.
        # В функции print() будет вызываться метод класса,
        # который соответствует введённой команде.
        if cmd in commands:
            print(commands[cmd])
        else:
            print('Нет такой команды. Введите attack/defence/special пажалста')


if __name__ == '__main__':
    """Start the app, run the screensaver, game starts on pressing 'X'.
    Args: None.
    Return: None.
    """
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_category = choice_char_class(char_name)
    start_training(char_category)
    # char_class: str = choice_char_class()
    # start_training(char_name, char_class)
