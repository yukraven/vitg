from Tools.LocationLoader import LocationLoader

locationLoader = LocationLoader(["Locations.json"])
location = locationLoader.getRandomLocation()

for i in range(1, 31):
    print("Turn %s:" % i, location())

