"""
GE 120 Machine Exercise 3
March 14, 2024
Lindsay Gutierrez 
2023-02961
"""

# as long as idedefine mo yung term before calling the function, oki lan yun
import math
from math import cos, sin, pi, radians, sqrt

def getLatitude(distance, azimuth) :
    lat = -(distance)*(cos(radians(azimuth)))
    return lat

def getDeparture(distance, azimuth) : 
    dep = -(distance)*(sin(radians(azimuth)))
    return dep
     

def azimuthToBearing(azimuth) : 
   if "-" in str(azimuth): # In case the input value of azimuth is in the form of dms
     degrees, minutes, seconds = azimuth.split("-")
     azimuth = ((int(degrees)) + (int(minutes)/60) + (float(seconds)/3600))%360
   else: 
     azimuth = float(azimuth)%360  

   if azimuth > 0 and azimuth < 90:
       azimuth_dms = azimuth
       degree = int(azimuth)
       minutes = (azimuth_dms - degree) * 60
       minutes_fractional = int(minutes)
       seconds = ((minutes - minutes_fractional) * 60)
       br_dms = str(degree)+ "-" + str(int(minutes)) + "-" + str(round(seconds,2))

       bearing = "S {: ^10} W".format(br_dms)
       #return bearing 

   elif azimuth > 90 and azimuth <180:
       azimuth_dms = 180 - azimuth

       degree = int(azimuth_dms)
       minutes = (azimuth_dms - degree) * 60
       minutes_fractional = int(minutes)
       seconds = ((minutes - minutes_fractional) * 60)
       br_dms = str(degree)+ "-" + str(int(minutes)) + "-" + str(round(seconds,2))

       bearing = "N {: ^10} W".format(br_dms)
       #return bearing 

   elif azimuth > 180 and azimuth <270: 
       azimuth_dms = azimuth - 180

       degree = int(azimuth_dms)
       minutes = (azimuth_dms - degree) * 60
       minutes_fractional = int(minutes)
       seconds = ((minutes - minutes_fractional) * 60)
       br_dms = str(degree)+ "-" + str(int(minutes)) + "-" + str(round(seconds,2))

       bearing = "N {: ^10} E".format(br_dms) 

   elif azimuth > 270 and azimuth <360:
       azimuth_dms = 360 - azimuth

       degree = int(azimuth_dms)
       minutes = (azimuth_dms - degree) * 60
       minutes_fractional = int(minutes)
       seconds = ((minutes - minutes_fractional) * 60)
       br_dms = str(degree)+ "-" + str(int(minutes)) + "-" + str(round(seconds,2))

       bearing = "S {: ^10} E".format(br_dms) 

   elif azimuth == 0:
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

counter = 1 # tells you from what line are we from 
count = 2 # tells you to what is the next line
lines = []
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
   
   bearingPrint = azimuthToBearing(azimuth)
   latPrint = getLatitude(distance = float(distance), azimuth = float(azimuth))
   depPrint = getDeparture(distance = float(distance), azimuth = float(azimuth)) 
   
   sumLat += latPrint #+= INCEREMENT
   sumDep += depPrint
   sumDist = float(distance)
   
   line = (str(counter) + "-" + str(count), distance, bearingPrint, latPrint, depPrint)
   lines.append(line)

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

# Corrections constants
ccorr_lat = -(sumLat)/sumDist
ccorr_dep = -(sumDep)/ sumDist

'''
for line in lines: 
    corr_lat = (ccorr_lat) * line[1]
    corr_dep = (ccorr_dep) * line[1]

    adjLat = line[3] + corr_lat
    adjDep = line[4] + corr_dep #here naging line[] sya dahil dun sa list sa 107, nandoon nakalagay yung latprint na lat na need ng corr
'''

# print the output
# summation of latitude, departure, distance
print("∑ Latitude: ", sumLat)
print("∑ Departure: ", sumDep)
print("∑ Distance: ", sumDist)

#LEC and REC
print("LEC: ",LEC)
print("REC: ", REC)


print("\n\nLines") # adds space after the question 'add new line'
print("{: ^12} {: ^18} {: ^20}  {: ^18} {: ^18}".format("LINE NO.", "DISTANCE", "BEARING, LATITUDE, DEPARTURE"))
for line in lines: # ibig sabihin para sa line na tuple (107) sa loob ng lines na list ang magiging format nya ay below
     print(' {: ^10}  | {: ^14}  | {: ^17} | {: ^14}  | {: ^14}  |'.format(line[0], line[1], line[2], line[3], line[4]))
print(' {: ^45}'.format("----------END-----------"))


# degree(atan(dep/lat))