import logging
import logging.config
from Sources.Tools.LocationLoader import LocationLoader
from Sources.Resources.Location import Location

logging.config.fileConfig("Logs/logging.conf")
logger = logging.getLogger("main")

locationLoader = LocationLoader(["Jsons/Locations.json"])
location = locationLoader.getRandomLocation()

logger.info("In main")

for i in range(1, 31):
    print("Turn %s:" % i, location())
