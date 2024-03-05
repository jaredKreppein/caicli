from shapely.geometry import Point, Polygon
from src.area import Area
import requests
from typing import List

# Client to retrieve and parse area data from the CAIC website.
class AreaClient:
    def __init__(self):
        self.regional_discussion_areas = []
        self.avalanche_areas = []
        self.special_product_areas = []

    def get_avalanche_area_id(self, point: Point) -> str | None:
        URL = "https://avalanche.state.co.us/api-proxy/avid?_api_proxy_uri=/products/all/area?productType=avalancheforecast&includeExpired=true"

        if len(self.avalanche_areas) == 0:
            self.avalanche_areas = self.__get_areas(URL)

        for area in self.avalanche_areas:
            if area.contains(point):
                return area.id     

        return None

    def get_special_product_id(self, point: Point) -> str | None:
        URL = "https://avalanche.state.co.us/api-proxy/avid?_api_proxy_uri=/products/all/area?productType=specialproduct&includeExpired=true"
        
        if len(self.special_product_areas) == 0:
            self.special_product_areas = self.__get_areas(URL)

        for area in self.special_product_areas:
            if area.contains(point):
                return area.id     

        return None
    
    def get_regional_discussion_id(self, point: Point) -> str | None:
        URL = "https://avalanche.state.co.us/api-proxy/avid?_api_proxy_uri=/products/all/area?productType=regionaldiscussion&includeExpired=true"
        
        if len(self.regional_discussion_areas) == 0:
            self.regional_discussion_areas = self.__get_areas(URL)

        for area in self.regional_discussion_areas:
            if area.contains(point):
                return area.id     

        return None
    
    def __get_areas(self, url: str) -> List[Area]:
        areas = self.__get_and_extract_areas(url)
        if areas is None:
            return []
        return areas

    def __get_and_extract_areas(self, url: str) -> List[Area] | None:
        areas = []

        try:
            response = requests.get(url)

            if response.status_code != 200:
                raise requests.exceptions.HTTPError(f"HTTP error occurred: {response.status_code}")

            data = response.json()
            for feature in data["features"]:
                id = feature["id"]

                polygons = []
                for shape_coordinates in feature["geometry"]["coordinates"]:
                    for coords in shape_coordinates:
                        coordinates_tuples = [tuple(coord) for coord in coords]
                        polygons.append(Polygon(coordinates_tuples))
                
                areas.append(Area(id, polygons))

            return areas

        except requests.exceptions.RequestException as e:
            print(f"Error occurred during the request: {e}")
            return None
