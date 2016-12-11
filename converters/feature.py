import shapely.geometry


class Feature:
    def __init__(self, geometry: shapely.geometry.base.BaseGeometry, tags: dict = None):
        """
        :type geometry: shapely.geometry.base
        """
        assert isinstance(geometry, shapely.geometry.base.BaseGeometry)
        self.geometry = geometry
        if tags:
            self._tags = tags
        else:
            self._tags = {}

    def set_tag(self, key: str, value: str):
        self._tags[key] = value

    def get_tag(self, key: str) -> str:
        return self._tags[key]

    @property
    def geojson(self):
        return {
            'type': "Feature",
            'geometry': shapely.geometry.mapping(self.geometry),
            'properties': self._tags
        }

    @property
    def tags(self):
        return self._tags

