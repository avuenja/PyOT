armadile = genMonster("Armadile", 487, 18378)
armadile.health(3800, healthmax=3800)
armadile.type("blood")
armadile.defense(armor=30, fire=0.80, earth=0, energy=0.85, ice=0.85, holy=0.85, death=1, physical=0.95, drown=1)
armadile.experience(2900)
armadile.speed(350)
armadile.behavior(summonable=0, hostile=True, illusionable=False, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
armadile.walkAround(energy=0, fire=1, poison=0)
armadile.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
armadile.voices("Creak!")
armadile.melee(400)