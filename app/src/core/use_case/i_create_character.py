from typing import List

from ..domain.interfaces.ICharacter import ICharacter
from ..domain.interfaces.ICharacterRepository import ICharacterRepository
from ..domain.model.Character import Character


class CreateCharacter:
    def __init__(self, dependencies):
        self.character_repository: ICharacterRepository = dependencies[
            "character_repository"
        ]

    def create_character(self, character: ICharacter):
        new_character = Character(character=character)
        print(new_character.id)
        return self.character_repository.create_character(character=new_character)
