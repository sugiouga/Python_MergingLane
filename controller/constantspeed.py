import config as Config

class Controller_ConstantSpeed:

    def __init__(self, vehicle, reference_velocityX_m_s):
        super().__init__(vehicle)
        self.reference_velocityX = reference_velocityX_m_s

        self.TIME_STEP = Config.TIME_STEP

    def update(self):
        # 車両の速度を一定に保つための加速度を計算する
        self.accX_input = (self.reference_velocityX - self.vehicle.get_velocityX()) / self.TIME_STEP
        self.vehicle.set_accX_input(self.accX_input)