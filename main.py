import json
import Resources as R

LocJs = json.load(open("Locations.json"))

for i in LocJs:
    temp = LocJs[i]
    location = R.Location(temp["startDescription"], temp["description"], temp["expectedCommands"],
                          temp["weather"], temp["weatherChances"], temp["weatherChanging"])
    for i in range(1, 31):
        print(("Location step %d: " % i) + location())
