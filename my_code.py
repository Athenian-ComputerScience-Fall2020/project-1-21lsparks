# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  Claryse Adams (tutor)



radish = ["radish", "acid", "high sun", "winter", "high water", "annual"]
lettuce = ["lettuce", "acid", "high sun", "winter", "high water", "annual"]
carrot = ["carrot", "acid", "high sun", "winter", "high water", "annual"]
corn = ["corn", "acid", "high sun", "winter", "high water", "annual"]
beans = ["beans", "acid", "low sun", "winter", "high water", "annual"]
#these are the lists storing information about each of the plants that we will use


plantlist = []
plantlist.append(radish)
plantlist.append(lettuce)
plantlist.append(carrot)
plantlist.append(corn)
plantlist.append(beans)

#list is a list of all of the plants that we'll reference to see if there's a match


print("Welcome! We want to help you plant. We will ask you a series of questions about plants and you will answer.")
#intro
plantsoil = input("If acidic, enter 'acid', if basic, enter 'basic'")
while plantsoil != "acid" and plantsoil != "basic":
    plantsoil = input("Invalid, try again:")
plantsun = input("If high sun, enter 'high sun', if low sun, enter 'low sun'")
while plantsun != "high sun" and plantsun != "low sun":
    plantsun = input("Invalid. Try again:")
plantseason = input("If winter, type 'winter'")
while plantseason != "winter" and plantseason != "summer" and plantseason != "spring" and plantseason != "fall":
    plantseason = input("Invalid. Do it again:")
planttyp = input("If annual, write 'annual'")
while planttyp != "annual" and planttyp != "perennial":
    planttyp = input("Invalid. Try again:")
plantwater = input("If high water, write 'high water'")
while plantwater != "high water" and plantwater != "low water":
    plantwater = input("No. Try Again:")

#this collects all of the information from the user on what type of conditions they plant needs to be able to grow in

plant = ["sample", plantsoil, plantsun, plantseason, plantwater, planttyp]
plantfound = False


#this creates a sample plant with all of the inputs that the user wants to check the real plants against

for p in plantlist:
    x = p
    if p[1] == plant[1]:
        if p[2] == plant[2]:
            if p[3] == plant[3]:
                if p[4] == plant[4]:
                    if p[5] == plant[5]:
                        plantfound = True
                        #this will mean that later when the program checks to see if there are any matches there are, and it doesn't print the sorry statement
                        print(f"Great! '{x[0]}' matches your search!")

#the above if statements check to see if all of the categories for a plant are the same as the input

if plantfound == False:
    print("Sorry! We have no plants that match your criteria, try again!")
# this checks to see if any plants match the inputs, if not, it will say there aren't any

plantdict = {"corn":corn, "carrot":carrot, "radish":radish, "lettuce":lettuce, "beans":beans}
#this connects the variable 'corn' to the list corn that we have in the beginning of the program so it will print if inputed
pickme = input("If you would like a complete profile on any plant, input it's name")

try:
    print("soil: %s" % (plantdict[pickme])[1])
    print("sun: %s" % (plantdict[pickme])[2])
    print("season: %s" %(plantdict[pickme])[3])
    print("water: %s" %(plantdict[pickme])[4])
    print("type: %s" %(plantdict[pickme])[5])
# this will print all of the information about any plant that we have once the user inputs it

except KeyError:
    print("Sorry, we didn't find anything for that!")
#this is to cover the error, to prevent it from crashing