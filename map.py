# Mapクラスは、道路の情報を管理するクラスです。
class map:
    def __init__(self):
        # 道路の情報を格納する辞書を初期化する
        # 道路のキーは道路ID、値は道路オブジェクト
        self.roads = {}

    # 道路の情報を取得するメソッド
    def get_roads(self):
        return self.roads

    def get_road(self, road_id):
        if road_id in self.roads:
            return self.roads[road_id]
        else:
            raise ValueError(f"Road with ID {road_id} does not exist.")

    def add_road(self, road):
        self.roads[road.road_id] = road

    def remove_road(self, road):
        if road.road_id in self.roads:
            del self.roads[road.road_id]

    def add_vehicle_to_road(self, vehicle_id, road_id, road_positionX_m, velocityX_m_s):
        if road_id in self.roads:
            road = self.roads[road_id]
            road.add_vehicle(vehicle_id, road_positionX_m, velocityX_m_s)
        else:
            raise ValueError(f"Road with ID {road_id} does not exist.")

    def remove_vehicle_from_road(self, vehicle_id):
        for road in self.roads.values():
            if vehicle_id in road.get_vehicles():
                road.remove_vehicle(vehicle_id)
                return
        raise ValueError(f"Vehicle with ID {vehicle_id} does not exist in any road.")

    def is_vehicle_at_end(self, vehicle_id, road_id):
        if road_id in self.roads:
            road = self.roads[road_id]
            return road.is_vehicle_at_end(vehicle_id)
        else:
            raise ValueError(f"Road with ID {road_id} does not exist.")

    def transfer_vehicle_new_road(self, old_road_id, next_road_id):
        if old_road_id in self.roads and next_road_id in self.roads:
            old_road = self.roads[old_road_id]
            next_road = self.roads[next_road_id]
            for vehicle_id, vehicle in old_road.get_vehicles().items():
                if vehicle.get_positionX() >= old_road.end_positionX:
                    next_road.add_vehicle(vehicle_id, vehicle.get_positionX(), vehicle.get_velocityX())
                    old_road.remove_vehicle(vehicle_id)
        else:
            raise ValueError(f"Road with ID {old_road_id} or {next_road_id} does not exist.")
