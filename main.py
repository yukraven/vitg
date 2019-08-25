import json
import Resources as R

LocJs = json.load(open("Locations.json"))

for i in LocJs:
    temp = LocJs[i]
    location = R.Location(temp["description"], temp["expectedCommands"],
                          temp["weather"])
    print(repr(location))
    print(location)
    print(location())


