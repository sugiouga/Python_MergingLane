import component.base_vehicle as Vehicle

# 道路クラス
class BaseRoad:

    def __init__(self, road_id, lane_number, start_positionX_m, end_positionX_m, mainlane_positionY):
        # 道路の物理的な特性を定義する
        self.LANEWIDTH = 3.5

        # 道路のID、車線数、開始位置、終了位置を設定する
        self.road_id = road_id
        self.lane_number = lane_number

        self.start_positionX = start_positionX_m
        self.end_positionX = end_positionX_m
        self.road_length = end_positionX_m - start_positionX_m

        self.mainlane_positionY = mainlane_positionY
        self.road_left_edge = self.mainlane_positionY + self.LANEWIDTH * (2 * lane_number - 1) /2
        self.road_right_edge = self.mainlane_positionY - self.LANEWIDTH /2

        # 道路上の車両を格納する辞書を初期化する
        # 車両のキーは車両ID、値は車両オブジェクト
        self.vehicles_in_road = {}

    # 道路の情報を取得するメソッド
    def get_road_id(self):
        return self.road_id

    def get_lane_number(self):
        return self.lane_number

    def get_vehicles(self):
        return self.vehicles_in_road

    def get_vehicle(self, vehicle_id):
        if vehicle_id in self.vehicles_in_road:
            return self.vehicles_in_road[vehicle_id]
        else:
            raise ValueError(f"Vehicle with ID {vehicle_id} does not exist.")

    def get_vehicle_road_positionX(self, vehicle_id):
        if vehicle_id in self.vehicles_in_road:
            vehicle = self.vehicles_in_road[vehicle_id]
            return vehicle.get_positionX() - self.start_positionX
        else:
            raise ValueError(f"Vehicle with ID {vehicle_id} does not exist.")

    # road_positionX_mは道路の開始位置からの距離を表す
    def add_vehicle(self, vehicle_id, road_positionX_m, velocityX_m_s):
        if vehicle_id not in self.vehicles_in_road:
            vehicle = Vehicle(vehicle_id, self.road_id, self.start_positionX + road_positionX_m, self.mainlane_positionY, velocityX_m_s, 0, None)
            self.vehicles_in_road[vehicle_id] = vehicle
        else:
            raise ValueError(f"Vehicle with ID {vehicle_id} already exists.")

    def remove_vehicle(self, vehicle_id):
        if vehicle_id in self.vehicles_in_road:
            del self.vehicles_in_road[vehicle_id]
        else:
            raise ValueError(f"Vehicle with ID {vehicle_id} does not exist.")

    # 車両が道路の終端に到達したかどうかを確認するメソッド
    # 車両の位置が道路の終端位置を超えた場合、Trueを返す
    def is_vehicle_at_end(self, vehicle_id):
        if vehicle_id in self.vehicles_in_road:
            vehicle = self.vehicles_in_road[vehicle_id]
            return vehicle.get_positionX() > self.end_positionX
        else:
            raise ValueError(f"Vehicle with ID {vehicle_id} does not exist.")

class SingleLaneRoad(BaseRoad):
    def __init__(self, road_id, start_positionX_m, end_positionX_m, mainlane_positionY):
        super().__init__(road_id, 1, start_positionX_m, end_positionX_m, mainlane_positionY)

class DoubleLaneRoad(BaseRoad):
    def __init__(self, road_id, start_positionX_m, end_positionX_m, mainlane_positionY):
        super().__init__(road_id, 2, start_positionX_m, end_positionX_m, mainlane_positionY)

class Lamp(BaseRoad):
    def __init__(self, road_id, start_positionX_m, end_positionX_m, mainlane_positionY):
        super().__init__(road_id, 2, start_positionX_m, end_positionX_m, mainlane_positionY)
        self.mergelane_start_positionX = start_positionX_m
        self.mergelane_end_positionX = end_positionX_m
        self.mergelane_positionY = mainlane_positionY + self.LANEWIDTH / 2