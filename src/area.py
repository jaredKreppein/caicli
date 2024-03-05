class Area:
    def __init__(self, id, polygons):
        self.id = id
        self.polygons = polygons
        self.type = type

    def contains(self, point):
        for polygon in self.polygons:
            if polygon.contains(point):
                return True
        return False
