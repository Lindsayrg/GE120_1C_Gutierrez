"""
GE 120 Machine Exercise 4
April 11, 2024
Lindsay Gutierrez 
2023-02961
"""

import math
from math import cos, sin, pi, radians, sqrt

'''
Starting from creating a class for the values needed to define the line to be surveyed.
Name the class as "Line"
'''

class Line: # under this class, we define three values: latitude, departure, and bearing

    def __init__(self, distance, azimuth):
        self.distance = distance 
        self.azimuth = azimuth 

    def latitude(self):
        '''
        Computing for the latitude of a line
        
        Input needed: 
        distance and azimuth (float)

        Expected output:
        latitude (float)
        '''

        lat = round(-float(self.distance)*(cos(radians(self.azimuth))),5)
        return lat

    def departure(self):
        '''
        Computing for the departure of a line
        
        Input needed: 
        distance and azimuth (float)

        Expected output:
        departure (float)
        '''

        dep = round(-float(self.distance)*(sin(radians(self.azimuth))),5)
        return dep

    def bearing(self): 

        if azimuth > 0 and azimuth < 90:
            azimuth_dms = azimuth
            degree = int(azimuth)
            minutes = (azimuth_dms - degree) * 60
            minutes_fractional = int(minutes)
            seconds = ((minutes - minutes_fractional) * 60)
            br_dms = str(degree)+ "-" + str(int(minutes)) + "-" + str(round(seconds,2))

            bearing = "S {: ^10} W".format(br_dms)
            return bearing 

        elif azimuth > 90 and azimuth <180:
            azimuth_dms = 180 - azimuth

            degree = int(azimuth_dms)
            minutes = (azimuth_dms - degree) * 60
            minutes_fractional = int(minutes)
            seconds = ((minutes - minutes_fractional) * 60)
            br_dms = str(degree)+ "-" + str(int(minutes)) + "-" + str(round(seconds,2))

            bearing = "N {: ^10} W".format(br_dms)
            return bearing 

        elif azimuth > 180 and azimuth <270: 
            azimuth_dms = azimuth - 180

            degree = int(azimuth_dms)
            minutes = (azimuth_dms - degree) * 60
            minutes_fractional = int(minutes)
            seconds = ((minutes - minutes_fractional) * 60)
            br_dms = str(degree)+ "-" + str(int(minutes)) + "-" + str(round(seconds,2))

            bearing = "N {: ^10} E".format(br_dms)
            return bearing 

        elif azimuth > 270 and azimuth <360:
            azimuth_dms = 360 - azimuth

            degree = int(azimuth_dms)
            minutes = (azimuth_dms - degree) * 60
            minutes_fractional = int(minutes)
            seconds = ((minutes - minutes_fractional) * 60)
            br_dms = str(degree)+ "-" + str(int(minutes)) + "-" + str(round(seconds,2))

            bearing = "S {: ^10} E".format(br_dms)
            return bearing

        else: 
            bearing = "Please input an azimuth value."
        return bearing

'''
We create a new class for bearing which lies on the cardinal directions
'''

class Cardinal(Line): 
    def __init__(self, distance, azimuth):
        super().__init__(distance, azimuth)
    
    def bearing(self):
        if azimuth == 0:
            bearing = "   DUE SOUTH  "
        elif azimuth == 90:
            bearing = "   DUE WEST  "
        elif azimuth == 180:
            bearing = "   DUE NORTH  "
        elif azimuth == 270:
            bearing = "   DUE EAST  "
        else: 
            bearing = "Please input an azimuth value."
        return bearing

#Sentinel controlled loop
counter = 1 # tells you from what line are we from 
count = 2 # tells you to what is the next line
lines = []
lines2 = []
lines3 = []
sumLat = 0 
sumDep = 0
sumDist = 0 

while True:
   print ()
   print("Line No.", counter, '-', counter + 1 )

   wrong_input = False
   while not(wrong_input): 
          distance = input('Distance: ')
          if wrong_input: 
            print("Invalid. Please input valid distance value")
            continue
          if not(wrong_input): 
            break
   azimuth = input("Azimuth from the South: ")

   if "-" in str(azimuth): # In case the input value of azimuth is in the form of dms
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = ((int(degrees)) + (int(minutes)/60) + (float(seconds)/3600))%360
   else: 
        azimuth = float(azimuth)%360    
   
   if azimuth % 90 == 0:
        line = Cardinal(distance, azimuth)
    
   else: 
        line = Line(distance, azimuth)

   sumLat += line.latitude()
   sumDep += line.departure()
   sumDist = float(line.distance)
   
   lines.append((str(counter) + "-" + str(count), line.distance, line.bearing(), line.latitude(), line.departure()))

# Ask for input
   yn = input("Add new line?")
   if yn.lower() == "yes" or yn.lower() == "y": # we can actually code it as - yes.lower 
      counter = counter + 1
      count = count + 1
      continue    
# to make sure that user will not accidentally finish the list, another question was asked to ensure the certainty of the following step
   else: 
       yn_2 = input("End traverse?")
       if yn_2.lower() == "y" or yn_2.lower() == "y":
          break
       else: 
          yn = input("Add new line?")
          if yn.lower() == "yes" or yn.lower() == "y":  
             counter = counter + 1
             count = count + 1
             continue  

LEC = sqrt((sumLat**2) + (sumDep**2))
REC = sumDist//LEC

line2 = (round(sumLat,5), round(sumDep,5), round(sumDist,5)) # for the table of the summation of values
lines2.append(line2)

#corrections code
'''
# Corrections constants
ccorr_lat = -(sumLat)/sumDist
ccorr_dep = -(sumDep)/ sumDist


for line in lines: 
    corr_lat = (ccorr_lat) * line[1]
    corr_dep = (ccorr_dep) * line[1]

    adjLat = line[3] + corr_lat
    adjDep = line[4] + corr_dep 


line3 = (str(counter) + "-" + str(count), round(corr_lat,5), round(corr_dep,5), round(adjLat,5), round(adjDep,5))
lines3.append(line3)
'''

print("\n\nLines") # adds space after the question 'add new line'
print("{: ^12} {: ^18} {: ^20}  {: ^14} {: ^24}".format("LINE NO.", "DISTANCE", "BEARING", "LATITUDE", "DEPARTURE"))
for line in lines: 
     print(' {: ^10}  | {: ^14}  | {: ^17} | {: ^14}   |  {: ^18}   |'.format(line[0], line[1], line[2], line[3], line[4]))

# print the output
# summation of latitude, departure, distance
print("\n\nSummation")
print("{: ^17} {: ^21} {: ^15} ".format("∑ Latitude", "∑ Departure", "∑ Distance"))
for line2 in lines2: 
     print(' {: ^15}  | {: ^15}  | {: ^17} |'.format(line2[0], line2[1], line2[2]))

#LEC and REC
print("\n")
print("LEC: ",round(LEC,5))
print("REC: ", REC)

#code for corrections table, unable to print other lines
'''
print("\n\nCorrections")
print("{: ^12}  {: ^12} {: ^23} {: ^23}  {: ^19}".format("LINE NO.", "Latitude Correction", "Departure Correction", "ADJUSTED LATITUDE", "ADJUSTED DEPARTURE"))
for line3 in lines3: 
     print(' {: ^10}  | {: ^15}    | {: ^19}  | {: ^20} | {: ^20} |'.format(line3[0], line3[1], line3[2], line3[3], line3[4]))
'''

print("\n\n")
print(' {: ^65}'.format("-------------END--------------"))


