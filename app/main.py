from app.constants.knights import KNIGHTS
from app.units.knight import Knight
from app.actions.battle import Battle

def battle(knights_config: dict) -> dict[str, int]:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot_stats = knights_config["lancelot"]
    lancelot = Knight(knight=lancelot_stats, protection=0)
    # apply armour
    lancelot.apply_armor()
    # apply weapon
    lancelot.apply_weapon()
    # apply potion if exist
    lancelot.apply_potion()

    # arthur
    arthur_stats = knights_config["arthur"]
    arthur = Knight(knight=arthur_stats, protection=0)
    # apply armour
    arthur.apply_armor()
    # apply weapon
    arthur.apply_weapon()
    # apply potion if exist
    arthur.apply_potion()

    # mordred
    mordred_stats = knights_config["mordred"]
    mordred = Knight(knight=mordred_stats, protection=0)
    # apply armour
    mordred.apply_armor()
    # apply weapon
    mordred.apply_weapon()
    # apply potion if exist
    mordred.apply_potion()

    # red_knight
    red_knight_stats = knights_config["red_knight"]
    red_knight = Knight(knight=red_knight_stats, protection=0)
    # apply armour
    red_knight.apply_armor()
    # apply weapon
    red_knight.apply_weapon()
    # apply potion if exist
    red_knight.apply_potion()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.hp -= Battle.fight(mordred.power, lancelot.protection)
    mordred.hp -= Battle.fight(lancelot.power, mordred.protection)
    # check if someone fell in battle
    lancelot.hp = Battle.check_hp_results(lancelot)
    mordred.hp = Battle.check_hp_results(mordred)

    # 2 Arthur vs Red Knight:
    arthur.hp -= Battle.fight(red_knight.power, arthur.protection)
    red_knight.hp -= Battle.fight(arthur.power, red_knight.protection)
    # check if someone fell in battle
    arthur.hp = Battle.check_hp_results(arthur)
    red_knight.hp = Battle.check_hp_results(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
