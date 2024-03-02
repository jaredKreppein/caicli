from shapely.geometry import Point, Polygon
from area import Area

# Define your point
point = Point(-105.57981453197924, 40.29002803433932) 
# point2 = Point(-106.1168106757955, 39.71245104307196)
point2 = Point(-106.14477539062499, 39.564066030219294)
# point2 = Point(-105.59080086010424, 40.084402352772926)
# point2 = Point(-107.08494148510424, 40.67441528033398)
SILVERTHORNE = Point(-106.07124281369431, 39.62920492943338)
VAIL = Point(-106.37769661205736, 39.640621690625785)


import requests
from shapely.geometry import Polygon

def get_and_extract_avalanche_areas():
    areas = []
    url = "https://avalanche.state.co.us/api-proxy/avid?_api_proxy_uri=%2Fproducts%2Fall%2Farea%3FproductType%3Davalancheforecast%26includeExpired%3Dtrue"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        data = response.json()
        for feature in data["features"]:
            id = feature["id"]

            polygons = []
            for shape_coordinates in feature["geometry"]["coordinates"]:
                for coords in shape_coordinates:
                    print(f'SAMPLE COORD: {coords[0]}')
                    coordinates_tuples = [tuple(coord) for coord in coords]
                    polygons.append(Polygon(coordinates_tuples))
            
            areas.append(Area(id, polygons, "avalanche_area"))

        return areas

    except requests.exceptions.RequestException as e:
        print(f"Error occurred during the request: {e}")
        return None

# Example usage:
avalanche_areas = get_and_extract_avalanche_areas()

for area in avalanche_areas:
    if area.contains(VAIL):
        print(f"Point is in area {area.id} of type {area.type}")

print("finishes")
