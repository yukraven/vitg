from Tools.LocationLoader import LocationLoader

locationLoader = LocationLoader(["Locations.json"])
location = locationLoader.getRandomLocation()

print(repr(location))

