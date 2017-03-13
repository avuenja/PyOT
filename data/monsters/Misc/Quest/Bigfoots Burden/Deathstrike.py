Deathstrike = genMonster("Deathstrike", 500, 16091) #mostly unknown
Deathstrike.health(250000)
Deathstrike.type("blood")
Deathstrike.defense(armor=100, fire=0.5, earth=0, energy=0.6, ice=0.6, holy=0.8, death=0.6, physical=0.75, drown=0.75)
Deathstrike.experience(40000)
Deathstrike.speed(700)
Deathstrike.behavior(summonable=0, hostile=True, illusionable=False, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
Deathstrike.walkAround(energy=0, fire=0, poison=0)
Deathstrike.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
Deathstrike.voices("Deeestructiooon!", "Maaahhhrrr!", "I am carnage incarnate!", "I've seen the light! And it was all engulfing fire!", "Taaake... this!")
Deathstrike.melee(2000)