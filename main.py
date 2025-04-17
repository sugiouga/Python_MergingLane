import config as Config
import component as Component
import controller as Controller
import simulation as Simulation
import record_vehicle_data as RecordData

TIME_STEP = Config.TIME_STEP

Map = Component.SingleLaneMap()

Map.add_vehicle("agent0", "road0", 0, 0, 0, Controller.ConstantSpeed())

Simulation = Simulation(map)

Simulation.reset()

total_time_s = 10.0

Simulation.run(total_time_s)
