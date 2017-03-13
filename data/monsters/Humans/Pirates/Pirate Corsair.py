pirate_corsair = genMonster("Pirate Corsair", 98, 6080)
pirate_corsair.health(675)
pirate_corsair.type("blood")
pirate_corsair.defense(armor=22, fire=1.1, earth=0.8, energy=1, ice=0.95, holy=0.9, death=1.05, physical=1, drown=1)
pirate_corsair.experience(350)
pirate_corsair.speed(230)
pirate_corsair.behavior(summonable=0, hostile=2, illusionable=True, convinceable=775, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0, targetChange=0)
pirate_corsair.walkAround(energy=1, fire=1, poison=1)
pirate_corsair.immunity(paralyze=1, invisible=0, lifedrain=1, drunk=1)
pirate_corsair.voices("Hiyaa!", "Give up!", "Plundeeeeer!")
pirate_corsair.melee(170)
pirate_corsair.distance(150, ANIMATION_THROWINGKNIFE, chance(21))
pirate_corsair.loot( ("throwing star", 53.75, 12), ("rum flask", 0.0025), (2148, 100, 88), ("sabre", 9.75), ("compass", 10.0), ("dark shield", 1.25), ("peg leg", 0.5), ("pirate boots", 0.25), ("hook", 0.5, 3), ("dark armor", 1.75), ("pirate backpack", 1.0), ("strong health potion", 0.75), ("eye patch", 0.5), ("pirate hat", 0.75), ("skull candle", 0.25), ("piggy bank", 0.25) )