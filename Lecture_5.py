#OBJECT ORIENTED PROGRAMMING

#Creating crayon
class Crayon: #always capitalize the first letter of the class name
    pass

redcrayon = Crayon()

#print(type(redcrayon))

#creating ML hero
class MLHero: 
    def __init__(self, name, description="Twilight Goddess", offense=80): 
        self.name = name
        self.description = description
        role = "Mage"
        self.role = role.upper()[0]
        self.specialty = "Damage/Poke"
        self.statistics = {
            "durability": 60,
            "offense": offense,
            "skill_effects": 50,
            "difficulty": 70
        }
    def __str__(self):
        return(self.name + ", the " + self.description)

    def __add__(self, other):
        return(self.name + " and " + other.name + " combined!")

    def __gt__(self, other):
        if (self.statistics["offense"] > other.statistics["offense"]):
            return(self.name + " ATTACKED AND WON!")
        else:
            return(self.name + " lost. " + other.name + " is too strong!")

    def skill(self):
        print(self.name +' used the attack!') #pinapalitan kung ano yung currently na ginagawa ng isang function

    def superskill(self, opponent):
        print(self.name +' used superskill against ' + opponent)

Lunox = MLHero("Lunox")
Aldous = MLHero("Aldous", "Demon Slayer")
#print(Aldous + Lunox)
print(Lunox > Aldous)
#print("hero name: ", hero.name)
#hero.skill()
#hero.superskill("Zilong") #ininput dito value nung opponent form line 27

# pag nakalimutan mo ilagay yung self function then sasabihin ay may kulang na attribute


class Spam:
    __egg=7

    def print_egg(self):
       print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
