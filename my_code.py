# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  


#hi
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

plantlist = [radish, lettuce, carrot, corn, beans]

print("Welcome! We want to help you plant. We will ask you a series of questions about plants and you will answer.")
plantsoil = input("If acidic, enter 'acid', if basic, enter 'basic'")
plantsun = input("If high sun, enter 'high sun', if low sun, enter 'low sun'")
plantseason = input("If winter, type 'winter'")
planttyp = input("If annual, write 'annual'")
plantwater = input("If high water, write 'high water'")

plant = Plant("sample", plantsoil, plantsun, plantseason, plantwater, planttyp)
plantfound = False

for p in plantlist:
    x = p
    if p.soil == plant.soil:
        if p.plantsun == plant.sun:
            if p.plantseason == plant.season:
                if p.plantwater == plant.water:
                    if p.planttyp == planttyp:
                        plantfound = True
                        print(f"Great! '{x.name}' matches your search!")

if plantfound == False:
    print("Sorry! We have no plants that match your criteria, try again!")