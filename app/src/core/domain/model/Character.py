from uuid import uuid4

from ..interfaces.ICharacter import GenderEnum, WorkEnum


class Character:
    def __init__(self, character):
        self.id = self.get_or_create_id(character)
        self.name = self.get_or_create_name(character)
        self.gender = self.get_or_create_gender(character)
        self.origin = self.get_or_create_origin(character)
        self.work = self.get_or_create_work(character)
        self.level = self.get_or_create_level(character)
        self.XP = self.get_or_create_XP(character)
        self.destiny_points = self.get_or_create_destiny_points(character)

    
    def get_or_create_id(self, character):
        if not id in character:
            return uuid4()
        return character.id

    def get_or_create_name(self, character):
        if not 'name' in character:
            return 'John Doe'
        return character['name']

    def get_or_create_gender(self, character):
        if not 'gender' in character:
            return GenderEnum.NO_SELECTION
        return character['gender']
    
    def get_or_create_origin(self, character):
        if not 'origin' in character:
            return GenderEnum.NO_SELECTION
        return character['origin']

    def get_or_create_work(self, character):
        if not 'work' in character:
            return WorkEnum.NO_SELECTION
        return character['work']

    def get_or_create_level(self, character):
        if not 'level' in character:
            return 1
        return character['level']

    def get_or_create_XP(self, character):
        if not 'XP' in character:
            return 0
        return character['XP']
    
    def get_or_create_destiny_points(self, character):
        if not 'destiny_points' in character:
            return 0
        return character['destiny_points']