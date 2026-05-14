from app.types.knight_type import KnightType


class Battle:
    def __init__(self, knight: KnightType) -> None:
        self.knight = knight

    @staticmethod
    def fight(power: int, protection: int) -> int:
        return power - protection

    def check_hp_results(self) -> int:
        return 0 if self.hp <= 0 else self.hp
