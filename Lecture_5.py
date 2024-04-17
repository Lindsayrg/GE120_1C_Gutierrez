#OBJECT ORIENTED PROGRAMMING

#Creating crayon
class Crayon: #always capitalize the first letter of the class name
    pass

redcrayon = Crayon()

#print(type(redcrayon))

#creating ML hero
class MLHero: 
    def __init__(self, name, description="Twilight Goddess"): 
        self.name = name
        self.description = description
        self.role = "Mage"
        self.specialty = "Damage/Poke"
        self.statistics = {
            "Durability": 60,
            "Offense": 80,
            "skill_effects": 50,
            "difficulty": 70
        }
    def __str__(self):
        return(self.name + ", the " + self.description)
    def __add__(self, other):
        return(self.name + " and " + other.name + " combined!")
    def skill(self):
        print(self.name +' used the attack!') #pinapalitan kung ano yung currently na ginagawa ng isang function

    def superskill(self, opponent):
        print(self.name +' used superskill against ' + opponent)

Lunox = MLHero("Lunox")
Aldous = MLHero("Aldous", "Demon Slayer")
print(Aldous + Lunox)
#print("hero name: ", hero.name)
#hero.skill()
#hero.superskill("Zilong") #ininput dito value nung opponent form line 27

# pag nakalimutan mo ilagay yung self function then sasabihin ay may kulang na attribute
