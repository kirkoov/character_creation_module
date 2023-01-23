"""
The same character creation module, yet with classes to carry on.
"""
from random import randint

# Global string literals
DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80

BLOCK_LINE = 'блокировал'
DAMAGE_UNIT = 'ед. урона'
DAMAGE_LINE: str = 'нанёс урон противнику, равный'
SPEC_SKILL_LINE: str = 'применил специальное умение'

ENTER_CMDS_LINE: str = ''.join(
    ['Введи одну из команд: attack — чтобы атаковать противника, ',
     'defence — чтобы блокировать атаку противника или special — чтобы',
     ' использовать свою суперсилу.',
     ])
ENTER_HERO_NAME_LINE: str = ''.join(
    ['Введи название персонажа, за которого хочешь играть: Воитель — warrior,',
     ' Маг — mage, Лекарь — healer: ',
     ])

MAGE_LINE: str = ''.join(['Маг — находчивый воин дальнего боя. Обладает ',
                          'высоким интеллектом.'])
HEALER_LINE: str = ''.join(['Лекарь — могущественный заклинатель. Черпает ',
                            'силы из природы, веры и духов.'])
APPR_CHOICE_LINE: str = ''.join(
    ['Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, чтобы ',
     'выбрать другого персонажа ',
     ])


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
        Return: a str representation of magic the character can cast.
        """
        return (f'{self.name} {SPEC_SKILL_LINE} '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        """Describe a character based on their class."""
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    """Create a Warrior instance of the Character class."""
    BRIEF_DESC_CHAR_CLASS: str = (' дерзкий воин ближнего боя.'
                                  ' Сильный, выносливый и отважный.')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    """Create a Mage instance of the Character class."""
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя.'
                             ' Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    """Create a Healer instance of the Character class."""
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель.'
                             ' Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'
