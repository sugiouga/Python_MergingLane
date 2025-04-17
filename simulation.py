import config  as Config
import component as Component

class Simulation:
    def __init__(self, agents, traffics, map):
        self.agents = agents
        self.traffics = traffics
        self.map = map
        self.simulation_time = 0.0

        self.TIME_STEP = Config.TIME_STEP

    def run(self, total_time_s):
        # Simulation loop
        for t in range(int(total_time_s / self.TIME_STEP)):
            self.step()
            self.simulation_time += self.TIME_STEP

    def step(self):
        for agent in self.agents.values():
            agent.update()

        for traffic in self.traffics.values():
            traffic.update()
