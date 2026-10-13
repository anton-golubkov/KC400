import xml.etree.ElementTree as ET
import json

points = []
fname = "20261012-102309.kml"
tree = ET.parse(fname)
root = tree.getroot()

ns = {"kml": "http://www.opengis.net/kml/2.2"}

for p in root.findall(".//kml:Placemark", ns):
    name = p.findtext("kml:name", default="Unnamed", namespaces=ns)
    coords = p.findtext(".//kml:Point/kml:coordinates", namespaces=ns)

    if coords:
        lon, lat, *alt = map(float, coords.strip().split(","))
        points.append({
            "name": name,
            "lon": lon,
            "lat": lat,
            "images": [],
        })
        print(f"Name: {name} | Longitude: {lon}, Latitude: {lat}")
with open(f"{fname}.json", "w") as f:
    f.write(json.dumps(points, indent=2))