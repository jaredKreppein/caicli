

class Area:
    def __init__(self, id, polygons, type):
        self.id = id
        self.polygons = polygons
        self.type = type

    def contains(self, point):
        for polygon in self.polygons:
            if polygon.contains(point):
                return True
        return False
