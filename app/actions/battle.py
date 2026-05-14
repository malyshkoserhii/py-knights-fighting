from app.types.knight_type import KnightType


class Battle:
    @staticmethod
    def fight(power: int, protection: int) -> int:
        return power - protection

    @staticmethod
    def check_hp_results(knight: KnightType) -> int:
        return 0 if knight.hp <= 0 else knight.hp
