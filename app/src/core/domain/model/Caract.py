from ..interfaces.ICharacter import PyCaract


class Caract:
    def __init__(self, caract: PyCaract):
        self.force = self.get_or_create_property(caract, "force", 10)
        self.charisma = self.get_or_create_property(caract, "charisma", 10)
        self.agility = self.get_or_create_property(caract, "agility", 10)
        self.intel = self.get_or_create_property(caract, "intel", 10)
        self.brave = self.get_or_create_property(caract, "brave", 10)

    def get_or_create_property(
        self, caract: PyCaract, property: str, default_property: int
    ) -> int:
        if not property in caract:
            return default_property
        return caract[property]
