from src.area_client import AreaClient
from shapely.geometry import Point

# Define your point
point = Point(-105.57981453197924, 40.29002803433932) 
# point2 = Point(-106.1168106757955, 39.71245104307196)
point2 = Point(-106.14477539062499, 39.564066030219294)
# point2 = Point(-105.59080086010424, 40.084402352772926)
# point2 = Point(-107.08494148510424, 40.67441528033398)
SILVERTHORNE = Point(-106.07124281369431, 39.62920492943338)
VAIL = Point(-106.37769661205736, 39.640621690625785)

area_client = AreaClient()
print(f'VAIL AVY AREA ID: {area_client.get_avalanche_area_id(VAIL)}')
print(f'VAIL Regional AREA ID: {area_client.get_regional_discussion_id(VAIL)}')
print(f'VAIL Special Report ID: {area_client.get_special_product_id(VAIL)}')
