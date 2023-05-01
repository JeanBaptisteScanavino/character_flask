from typing import List
from uuid import uuid4

from ..interfaces.ICharacter import (GenderEnum, OriginEnum, PyCaract, PyMoney,
                                     PyObjectInInventory, WorkEnum)
from .Caract import Caract
from .Inventory import Inventory
from .Money import Money


class Character:
    def __init__(self, character):
        self.id = self.get_or_create_property(character, "id", uuid4())
        self.name = self.get_or_create_property(character, "name", "John Doe")
        self.gender = self.get_or_create_property(
            character, "gender", GenderEnum.NO_SELECTION
        )
        self.origin = self.get_or_create_property(
            character, "origin", OriginEnum.NO_SELECTION
        )
        self.work = self.get_or_create_property(
            character, "work", WorkEnum.NO_SELECTION
        )
        self.level = self.get_or_create_property(character, "level", 1)
        self.XP = self.get_or_create_property(character, "XP", 0)
        self.destiny_points = self.get_or_create_property(
            character, "destiny_points", 0
        )
        self.caract = self.get_or_create_caract(character)
        self.money = self.get_or_create_money(character)
        self.inventory = self.get_or_create_property(character, "inventory", [])

    def get_or_create_caract(self, character) -> PyCaract:
        if not "caract" in character:
            return Caract({})
        return Caract(character["caract"])

    def get_or_create_money(self, character) -> PyMoney:
        if not "money" in character:
            return Money({})
        return Money(character["money"])

    def get_or_create_property(
        self,
        character,
        property: str,
        default_property: str | int | OriginEnum | WorkEnum | GenderEnum,
    ) -> str | int | OriginEnum | WorkEnum | GenderEnum:
        if not property in character:
            return default_property
        return character[property]

    def get_or_create_inventory(self, character) -> List[PyObjectInInventory]:
        if not "inventory" in character:
            return Inventory([])
        return Inventory(character["inventory"])

    @property
    def magic_resistance(self) -> int:
        return (self.caract.force + self.caract.brave + self.caract.intel) // 3
