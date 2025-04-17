
# BaseMapクラスは、道路の情報を管理するクラスです。
class BaseMap:
    def __init__(self):
        # 道路の情報を格納する辞書を初期化する
        # 道路のキーは道路ID、値は道路オブジェクト
        self.roads_in_map = {}

    # 道路の情報を取得するメソッド
    def get_roads(self):
        return self.roads_in_map

    def get_road(self, road_id):
        if road_id in self.roads_in_map:
            return self.roads_in_map[road_id]
        else:
            raise ValueError(f"Road with ID {road_id} does not exist.")

    def add_road(self, road):
        self.roads_in_map[road.road_id] = road

    def remove_road(self, road):
        if road.road_id in self.roads_in_map:
            del self.roads_in_map[road.road_id]

    def get_vehicles(self):
        vehicles = {}
        for road_id in self.roads_in_map.keys():
            road = self.roads_in_map[road_id]
            vehicles.update(road.get_vehicles())
        return vehicles

    def get_vehicle(self, vehicle_id):
        for road in self.roads_in_map.values():
            if vehicle_id in road.get_vehicles():
                return road.get_vehicle(vehicle_id)
        raise ValueError(f"Vehicle with ID {vehicle_id} does not exist in any road.")

    def add_vehicle(self, vehicle_id, road_id, road_positionX_m, road_positionY_m, velocityX_m_s, controller):
        if road_id in self.roads_in_map:
            road = self.roads_in_map[road_id]
            road.add_vehicle(vehicle_id, road_positionX_m, road_positionY_m, velocityX_m_s, controller)
        else:
            raise ValueError(f"Road with ID {road_id} does not exist.")

    def remove_vehicle(self, vehicle_id):
        for road in self.roads_in_map.values():
            if vehicle_id in road.get_vehicles():
                road.remove_vehicle(vehicle_id)
                return
        raise ValueError(f"Vehicle with ID {vehicle_id} does not exist in any road.")

    # 終端に到達した車両を次の道路に移動するメソッド
    def transfer_vehicle_to_new_road(self, old_road_id, new_road_id):
        if old_road_id in self.roads_in_map and new_road_id in self.roads_in_map:
            _old_road = self.roads_in_map[old_road_id]
            _new_road = self.roads_in_map[new_road_id]
            for vehicle_id, vehicle in _old_road.get_vehicles().items():
                if _old_road.is_vehicle_at_end(vehicle_id):
                    # 車両の位置を次の道路に移動する
                    new_road_positionX_m = vehicle.get_road_positionX() - _old_road.road_length
                    new_road_positionY_m = vehicle.get_road_positionY()
                    _new_road.add_vehicle(vehicle_id, new_road_positionX_m, new_road_positionY_m, vehicle.get_velocityX())
                    _old_road.remove_vehicle(vehicle_id)
        else:
            raise ValueError(f"Road with ID {old_road_id} or {new_road_id} does not exist.")
