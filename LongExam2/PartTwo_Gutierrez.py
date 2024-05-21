'''
Lindsay Gutierrez
2023-02961
Long Exam 2 
Coding part-OOP
'''

'''
Part 1 pseudocode
Input: area(int), owner's name(string)

classify the lot based on the size(area)

Output: classification of land, owner's name

'''

class Parcel:
    def __init__(self, owner, area):
        self.owner = owner
        self.area = area

    def getclassification(self, area): #since the classification of area has certain ranges of values before it changes then we use the if-else statements
        if area < 10000: 
            classification = "Residential"
            return classification

        elif area >= 10000 and area < 120000: 
            classification = "Private Agricultural"
            return classification

        elif area >= 120000: 
            classification = "Public Agricultural"
            return classification
    
    def __str__(self): 
        return ( "A parcel of land owned by " + self.owner + " with an area of " + str(self.area) + " square meters." )

    def __add__(self, other, otherArea = 200 ): # input other area here
        totalArea = int(self.area) + int(otherArea) 
        return ( "Consolidated lot of " + self.owner + " and " + other.owner + " with total area of " +  str(totalArea) + " square meters.")

class Riparian(Parcel): 
    def __init__(self, owner, area):
        super().__init__(owner, area)
    
    def getAdjoiningWaterbody(self, type): 

        if type == 1:
            return ("Adjacent to River - can be subject to tilting")

        elif type == 2: 
            return ("Adjacent to Ocean (Littoral) - cannot be subject to tilting")

        else: 
            return("Invalid Ripirian Parcel")

#print output examples -- input value/names here 
Lindsay = Parcel("Lindsay", 100)
Gutierrez =Riparian("Lindsay", 100)
#Gutierrez =Parcel("Gutierrez", 200) #input other area and other owner name here
Lindsay.getclassification(100)
Gutierrez.getAdjoiningWaterbody(2)

print(Lindsay)
print(Lindsay.getclassification(100))
print(Gutierrez)
print(Gutierrez.getAdjoiningWaterbody(2))






