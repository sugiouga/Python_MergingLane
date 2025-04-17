import config  as Config
import component as Component
import save_data as SaveData

class Simulation:
    def __init__(self, map):
        self.map = map
        self.simulation_time = 0.0

        self.record = {}
        self._init_map = self.map.copy()

        self.TIME_STEP = Config.TIME_STEP

    def reset(self):
        # マップの情報をリセットする
        self.map.clear()

        # シミュレーション時間をリセットする
        self.simulation_time = 0.0

    def run(self, total_time_s):
        self.map = self.init_map.copy()

        # Simulation loop
        for t in range(int(total_time_s / self.TIME_STEP)):
            self.step()

            self.record[t] = self.map.get_vehicles()

            self.simulation_time += self.TIME_STEP

        SaveData.save_simulation_data

    def step(self):
        # Update all vehicles in the map
        for road in self.map.get_roads():
            for vehicle in road.get_vehicles().values():
                vehicle.update()

        # Update simulation time
        self.simulation_time += self.TIME_STEP


