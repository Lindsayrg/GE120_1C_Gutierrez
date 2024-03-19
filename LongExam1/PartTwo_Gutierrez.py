'''
Lindsay Gutierrez
2023-02961
Long Exam 1 
Coding part
'''
# Creating the functions
def floatInput (prompt):
    prompt_out = float(prompt)
    return prompt_out

# Defining the variables
levelling_table = []
total_distance = float(0)
tp_counter = 1
tpLabel = "TP"
bmLabel = "BM"

# Printing the title
print("Circuit Traverse" + "By: Lindsay Gutierrez")
print("\n\n")
print("This is a program that performs direct levelling computations of a circuit traverse.")
print("Traverse Stations", tp_counter, '-', tp_counter + 1 )
 
prompt = input('Elevation of BM: ') #here is where we input the known elevation of the Benchmark
tpElev = input("Elevation of next TP: ")

while True: 
    print("Traverse Stations ", tp_counter, '-', tp_counter + 1 )

    wrongBS = False
    while not(wrongBS): 
          prompt1 = input('Backsight in meters: ')
          prompt2 = input('Foresight in meters: ') 
          prompt3 = input('Distance: ')
          if wrongBS: 
            print("Invalid. Please input valid distance value") #add these to invalidate unacceptable inputs
            continue
          if not(wrongBS): 
            break
    fsm = floatInput(prompt2)
    bsm = floatInput(prompt1)
    dist = floatInput(prompt3)

    #Height of the instrument
    HI = float(tpElev) + bsm

    #New running Elev
    NewElev = float(HI) - fsm

    total_distance += dist


    line = (str(tp_counter), bsm, HI, fsm, NewElev) # with this we as we add new measurment of bsm, fsm, and hi, new elev, new lines are added in the list
    levelling_table.append(line)


# Ask for input
    yn = input("Add new measurement?")
    if yn.lower() == "yes" or yn.lower() == "y": # if the answer is yes in other format, it can still be validated
        yn2 = input("Is it a turning point?")
        if yn.lower() == "yes" or yn.lower() == "y":
            tp_counter = tpLabel + tp_counter + 1
            continue
        else: 
            tp_counter = bmLabel + tp_counter
            continue    
    else: 
        if yn.lower() == "no" or yn.lower() == "n": # if the user answers a no
            break

# print the output
print("\n\nlevelling_table") 
print("{: ^12} {: ^18} {: ^20}".format("Sta.", "B.S", "H.I", "F.S", "Elev"))
for line in levelling_table: 
     print(' {: ^10}  | {: ^14}  | {: ^17} | {: ^17} |  {: ^17} |'.format(line[0], line[1], line[2], line[3], line[4]))
print(' {: ^45}'.format("----------END-----------"))


#Error compute       
BM1_int = input("Initial Elevation of BM 1: ")
BM1_fin = input("Final Elevation of BM 1: ")

Error = BM1_fin - BM1_int
relError = 1/int(Error)

total_distance = total_distance/1000

if relError > 1/100000:
    VA = 4.80*sqrt(total_distance)
    orderClass = "First Order"
elif relError < 1/100000 and > 1/50000:
    VA = 8.40*sqrt(total_dist)
    orderClass = "Second Order"
elif relError < 1/50000 and > 1/20000:
    VA = 12.0*sqrt(total_dist)
    orderClass = "Third Order"
elif relError < 1/20000:
    VA = "invalid"
    orderClass = "ERROR TOO LARGE"
else:
    orderClass = "Pls input Elevation measurements"

print("Vertical Accuracy: ", VA)
print("Class Order: ", orderClass)





        





