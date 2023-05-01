from abc import ABCMeta, abstractmethod

from .ICharacter import PyCharacter


class ICharacterRepository(ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def create_character(character: PyCharacter):
        pass
