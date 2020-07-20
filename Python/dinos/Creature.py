"""Creature Classes"""

class Creature():

    def __init__(self, name, noise="Hmmph"):
        self.name = name
        self._noise = noise

    def speak() -> str:
        return self._noise

