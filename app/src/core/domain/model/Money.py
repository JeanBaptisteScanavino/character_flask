from ..interfaces.ICharacter import PyMoney


class Money:
    def __init__(self, money: PyMoney) -> None:
        self.gold = self.get_or_create_property(money, "gold", 0)
        self.silver = self.get_or_create_property(money, "silver", 0)
        self.thritil = self.get_or_create_property(money, "thritil", 0)
        self.berylium = self.get_or_create_property(money, "berylium", 0)

    def get_or_create_property(
        self, money: PyMoney, property: str, default_property: int
    ) -> int:
        if not property in money:
            return default_property
        return money[property]
