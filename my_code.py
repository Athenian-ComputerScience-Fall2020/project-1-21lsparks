# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  Claryse Adams (tutor)


class Plant:
    def __init__(self, name, soil, sun, season, water, typ):
        self.name = name
        self.soil = soil
        self. sun = sun
        self.season = season
        self.water = water
        self.typ = typ


radish = Plant("radish", "acid", "high sun", "winter", "high water", "annual")
lettuce = Plant("lettuce", "acid", "high sun", "winter", "high water", "annual")
carrot = Plant("carrot", "acid", "high sun", "winter", "high water", "annual")
corn = Plant("corn", "acid", "high sun", "winter", "high water", "annual")
beans = Plant("beans", "acid", "low sun", "winter", "high water", "annual")

plantlist = []
plantlist.append(radish)
plantlist.append(lettuce)
plantlist.append(carrot)
plantlist.append(corn)
plantlist.append(beans)


print("Welcome! We want to help you plant. We will ask you a series of questions about plants and you will answer.")
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

plant = Plant("sample", plantsoil, plantsun, plantseason, plantwater, planttyp)
plantfound = False

for p in plantlist:
    x = p
    if p.soil == plant.soil:
        if p.sun == plant.sun:
            if p.season == plant.season:
                if p.water == plant.water:
                    if p.typ == plant.typ:
                        plantfound = True
                        print(f"Great! '{x.name}' matches your search!")
if plantfound == False:
    print("Sorry! We have no plants that match your criteria, try again!")

plantdict = {"corn":corn, "carrot":carrot, "radish":radish, "lettuce":lettuce, "beans":beans}
pickme = input("If you would like a complete profile on any plant, input it's name")
try:
    print("soil: %s" % (plantdict[pickme]).soil)
    print("sun: %s" % (plantdict[pickme]).sun)
    print("season: %s" %(plantdict[pickme]).season)
    print("water: %s" %(plantdict[pickme]).water)
    print("type: %s" %(plantdict[pickme]).typ)

except KeyError:
    print("Sorry, we didn't find anything for that!")