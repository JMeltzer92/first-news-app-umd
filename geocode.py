import requests
import csv
import time

API_KEY = "9961afcf74eddccdd677f1527c67cfbd3ef7a45b"

base_url = f"https://api.geocodify.com/v2/geocode?api_key={API_KEY}&q="

results = []

with open("balt_city_22_overdoses.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        time.sleep(1)
        r = requests.get(base_url + row['location'])
        print(row['location'])
        if len(r.json()['response']['features']) > 0:
            lng, lat = r.json()['response']['features'][0]['geometry']['coordinates']
        else:
            lng = None
            lat = None
        results.append([row['recordId'], row['callKey'], row['callDateTime'], row['priority'], row['district'], row['description'], row['callNumber'], row['incidentLocation'], row['location'], row['Neighborhood'], row['PoliceDistrict'], row['PolicePost'], row['CouncilDistrict'], row['SheriffDistricts'], row['Community_Statistical_Areas'], row['Census_Tracts'], row['VRIZones'], row['ZIPCode'], row['NeedsSync'], row['IsDeleted'], row['ESRI_OID'], lat, lng])


with open("balt_city_22_overdoses_geo.csv", "w") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['recordId', 'callKey', 'callDateTime', 'priority', 'district', 'description', 'callNumber', 'incidentLocation', 'location', 'Neighborhood', 'PoliceDistrict', 'PolicePost', 'CouncilDistrict', 'SheriffDistricts', 'CommunityStatisticalAreas', 'Census_Tracts', 'VRIZones', 'ZIPCode', 'NeedsSync', 'IsDeleted', 'ESRI_OID', 'lat', 'lng'])
    writer.writerows(results)