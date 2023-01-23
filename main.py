"""
The same character creation module, yet with classes to carry on.
"""
from random import randint

# Global string literals
DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10

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
WARRIOR_LINE: str = ''.join(['Воитель — дерзкий воин ближнего боя. Сильный, ',
                             'выносливый и отважный.'])
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

    # Score range constants.
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15

    def __init__(self, name):
        self.name = name

    def attack(self):
        """Attack to be later overridden per hero.
        Args: hero name, hero class.
        Return: a str representation of damage a hero can do.
        """
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} {DAMAGE_LINE} {value_attack}'

    def defence(self):
        """Defence per hero.
        Args: hero name, hero class.
        Return: a str representation of defence a hero is capable of as per
        their class."""
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} {BLOCK_LINE} {value_defence} {DAMAGE_UNIT}.')

    def special(self):
        """Use a special skill per hero.
        Args: hero name, hero class.
        Return: a str representation of magic the hero can cast.
        """
        return (f'{self.name} {SPEC_SKILL_LINE} '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')


class Warrior(Character):
    """Create a Warrior instance based on the Character class."""
    ...


class Mage(Character):
    """Create a Mage instance based on the Character class."""
    ...


class Healer(Character):
    """Create a Healer instance based on the Character class."""
    ...
