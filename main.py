import json
import Resources.Location as L

LocJs = json.load(open("Locations.json"))

for i in LocJs:
    temp = LocJs[i]
    location = L.Location(temp["startDescription"], temp["description"], temp["expectedCommands"],
                          temp["weather"], temp["weatherChances"], temp["weatherChanging"])
    print(repr(location))
    for j in range(1, 31):
        print(("Location step %d: " % j) + location())

