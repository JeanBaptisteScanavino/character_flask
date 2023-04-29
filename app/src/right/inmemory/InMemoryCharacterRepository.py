from ...core.domain.interfaces.ICharacter import GenderEnum, ICharacter, OriginEnum
from uuid import uuid4

class DummyCharacter:
    def __init__(self, character:ICharacter):
        self.id = self.get_my_id()
        self.name = self.set_my_name(character)
        self.gender = self.set_my_gender(character)
        self.origin = self.set_my_origin(character)

    def get_my_id(self):
        return uuid4()

    def set_my_name(self, character:ICharacter):
        return character['name'] if 'name' in character else 'John Doe'
    
    def set_my_gender(self, character:ICharacter):
        return character['gender'] if 'gender' in character else GenderEnum.NO_SELECTION

    def set_my_origin(self, character:ICharacter):
        return character['origin'] if 'origin' in character else OriginEnum.NO_SELECTION

    def create_character(self):
        return self


class InMemoryCharacterRepository:
    def create_character(character):
        character.id = uuid4()
        return character
