from Tools.LocationLoader import LocationLoader
from Resources.Location import Location

locationLoader = LocationLoader(["Locations.json"])
location = locationLoader.getRandomLocation()

for i in range(1, 31):
    print("Turn %s:" % i, location())

location = Location()