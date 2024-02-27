"""
GE 120 Machine Exercise 1
February 27,2024
Lindsay Gutierrez 
2023-02961
"""

"""
Decimal degrees to DMS form
"""

# Set the variable, the input will be dd_input = input
dd_input = 118.42069

# We get the degree part uing either int or floor division 
degree = int(dd_input)

# We get the minutes part
minutes = (dd_input - degree) * 60

minutes_fractional = int(minutes)

# We get the seconds part
seconds = (minutes - minutes_fractional) * 60

# To get the DMS form with the required decimal places, we can usethe round command for the seconds part, and int for the minutes part

print("Input(Decimal degree): ", dd_input)
print("DMS: " + str(degree)+ "-" + str(int(minutes)) + "-" + str(round(seconds,2)))

"""
DMS form to Decimal degrees
"""

# Set the variable, the input must be string type
dms_input = "118-25-14.48"
values = dms_input.split("-")

# To access the integer values individually in the list, we use the list[index] command
degree = int(values[0])
minutes = int(values[1])
seconds = float(values[2])

dd = degree + (minutes/60) + (seconds/3600)

print("Input(DMS): ", dms_input)
print("Decimal degree: ", round(dd,6))