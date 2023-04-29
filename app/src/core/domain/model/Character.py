from uuid import uuid4

from ..interfaces.ICharacter import GenderEnum, OriginEnum, WorkEnum


class Caract:
    def __init__(self, caract):
        self.force = self.get_or_create_property(caract, "force", 10)
        self.charisma = self.get_or_create_property(caract, "charisma", 10)
        self.agility = self.get_or_create_property(caract, "agility", 10)
        self.intel = self.get_or_create_property(caract, "intel", 10)
        self.brave = self.get_or_create_property(caract, "brave", 10)

    # def get_or_create_force(self, caract):
    #     if not 'force' in caract:
    #         return 10
    #     return caract['force']
    # def get_or_create_charisma(self, caract):
    #     if not 'charisma' in caract:
    #         return 10
    #     return caract['charisma']
    # def get_or_create_agility(self, caract):
    #     if not 'agility' in caract:
    #         return 10
    #     return caract['agility']
    # def get_or_create_intel(self, caract):
    #     if not 'intel' in caract:
    #         return 10
    #     return caract['intel']
    # def get_or_create_brave(self, caract):
    #     if not 'brave' in caract:
    #         return 10
    #     return caract['brave']
    def get_or_create_property(self, caract, property: str, default_property: int):
        if not property in caract:
            return default_property
        return caract[property]


class Money:
    def __init__(self, money) -> None:
        self.gold = self.get_or_create_property(money, "gold", 0)
        self.silver = self.get_or_create_property(money, "silver", 0)
        self.thritil = self.get_or_create_property(money, "thritil", 0)
        self.berylium = self.get_or_create_property(money, "berylium", 0)

    # def get_or_create_gold(self, caract):
    #     if not 'gold' in caract:
    #         return 0
    #     return caract['gold']
    # def get_or_create_silver(self, caract):
    #     if not 'silver' in caract:
    #         return 0
    #     return caract['silver']
    # def get_or_create_thritil(self, caract):
    #     if not 'thritil' in caract:
    #         return 0
    #     return caract['thritil']
    # def get_or_create_berylium(self, caract):
    #     if not 'berylium' in caract:
    #         return 0
    #     return caract['berylium']
    def get_or_create_property(self, money, property: str, default_property: int):
        if not property in money:
            return default_property
        return money[property]


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

    # def get_or_create_id(self, character):
    #     if not id in character:
    #         return uuid4()
    #     return character.id

    # def get_or_create_name(self, character):
    #     if not 'name' in character:
    #         return 'John Doe'
    #     return character['name']

    # def get_or_create_gender(self, character):
    #     if not 'gender' in character:
    #         return GenderEnum.NO_SELECTION
    #     return character['gender']

    # def get_or_create_origin(self, character):
    #     if not 'origin' in character:
    #         return OriginEnum.NO_SELECTION
    #     return character['origin']

    # def get_or_create_work(self, character):
    #     if not 'work' in character:
    #         return WorkEnum.NO_SELECTION
    #     return character['work']

    # def get_or_create_level(self, character):
    #     if not 'level' in character:
    #         return 1
    #     return character['level']

    # def get_or_create_XP(self, character):
    #     if not 'XP' in character:
    #         return 0
    #     return character['XP']

    # def get_or_create_destiny_points(self, character):
    #     if not 'destiny_points' in character:
    #         return 0
    #     return character['destiny_points']

    def get_or_create_caract(self, character):
        if not "caract" in character:
            return Caract({})
        return Caract(character["caract"])

    def get_or_create_money(self, character):
        if not "money" in character:
            return Money({})
        return Money(character["money"])

    def get_or_create_property(
        self,
        character,
        property: str,
        default_property: str | int | OriginEnum | WorkEnum | GenderEnum,
    ):
        if not property in character:
            return default_property
        return character[property]

    @property
    def magic_resistance(self):
        return sum[self.caract.force, self.caract.brave, self.caract.intel]
