from uuid import uuid4

from ...core.domain.interfaces.ICharacter import (GenderEnum, OriginEnum,
                                                  PyCharacter)


class DummyCharacter:
    def __init__(self, character: PyCharacter):
        self.id = self.get_my_id()
        self.name = self.set_my_name(character)
        self.gender = self.set_my_gender(character)
        self.origin = self.set_my_origin(character)

    def get_my_id(self):
        return uuid4()

    def set_my_name(self, character: PyCharacter):
        return character["name"] if "name" in character else "John Doe"

    def set_my_gender(self, character: PyCharacter):
        return character["gender"] if "gender" in character else GenderEnum.NO_SELECTION

    def set_my_origin(self, character: PyCharacter):
        return character["origin"] if "origin" in character else OriginEnum.NO_SELECTION

    def create_character(self):
        return self


FAKE_INVENTORY = ["Shuriken of Destiny", "Wood Log"]
FAKE_SKILLS = ["Clone", "Eat lot of ramen"]


class InMemoryCharacterRepository:
    def create_character(character: PyCharacter):
        character.id = uuid4()
        if len(character.inventory) > 0:
            new_inventory = []
            for i, item_id in enumerate(character.inventory):
                new_inventory.append({"id": item_id, "name": FAKE_INVENTORY[i]})
            character.inventory = new_inventory
        if len(character.skills) > 0:
            new_skill = []
            for i, skill in enumerate(character.skills):
                new_skill.append({"id": skill, "name": FAKE_SKILLS[i]})
            character.skills = new_skill
        return character
