from typing import List

from ..domain.interfaces.ICharacter import ICharacter
from ..domain.interfaces.ICharacterRepository import ICharacterRepository


class CreateCharacter:
    def __init__(self, dependencies):
        self.character_repository: ICharacterRepository = dependencies[
            "character_repository"
        ]

    def create_character(self, character: ICharacter):
        return self.character_repository.create_character(character=character)
