import urllib2
import json
from subprocess import call
import shlex

# weatherStationsResponse = urllib2.urlopen("https://api.weather.gov/stations").read()
# with open("weatherStationsData.json", "wb") as weatherStationsData:
#     for weatherStationsDataChunk in weatherStationsData.iter_content(chunkSize=128):
#         weatherStationsData.write(weatherStationsDataChunk)

stationFilepaths = []

with open("weatherStationsData.json", "rb") as weatherStationsData:
    weatherStations = json.load(weatherStationsData)["features"]
    for i in range(2):
        stationUrl = weatherStations[i]["id"]
        print stationUrl
        # headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
        # observationsRequest = urllib2.Request(stationId + "/observations", headers=headers)
        # observations = urllib2.urlopen(observationsRequest);

        stationUrlSegments = stationUrl.split("/")
        stationCode = stationUrlSegments[len(stationUrlSegments) - 1]

        stationFilepaths.append("observations/observations-" + stationCode + ".json")
        call(shlex.split("sh download-cities-observations.sh " + stationUrl + " " + stationCode))

for stationFilepath in stationFilepaths:
    with open(stationFilepath) as observationsData:
            observations = json.load(observationsData)
            print observations

        
