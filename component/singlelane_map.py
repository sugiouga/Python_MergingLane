import base_road as SingleLaneRoad
import base_map as BaseMap

class SingleLaneMap(BaseMap):
    def __init__(self):
        super().__init__(self)

        BaseMap.add_road(SingleLaneRoad(0, 0, 1000, 0))