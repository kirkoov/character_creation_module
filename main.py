class Character:
    """Create a character basic for others to inherit from."""

    def __init__(self, name):
        self.name = name

    def attack(self):
        pass

    def defence(self):
        pass

    def special(self):
        pass


class Warrior(Character):
    """Create a Warrior instance based on the Character class."""
    ...


class Mage(Character):
    """Create a Mage instance based on the Character class."""
    ...


class Healer(Character):
    """Create a Healer instance based on the Character class."""
    ...
