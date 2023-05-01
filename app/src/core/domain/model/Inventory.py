from typing import List
from uuid import uuid4

from ..interfaces.ICharacter import PyObjectInInventory


class Inventory:
    def __init__(self, inventory: List[uuid4]):
        self.inventory = self.get_object(inventory)

    def get_object(self, inventory: List[uuid4]) -> PyObjectInInventory:
        construct_inventory = []
        for object_id in inventory:
            construct_inventory.append(ObjectRepository.get_object_name(object_id))
        return construct_inventory
