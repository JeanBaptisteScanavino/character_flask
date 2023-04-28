from abc import ABCMeta, abstractmethod

from .ICharacter import ICharacter


class ICharacterRepository(ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def create_character(character: ICharacter):
        pass
