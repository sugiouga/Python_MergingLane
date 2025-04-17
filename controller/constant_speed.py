class Controller_ConstantSpeed:

    def __init__(self, vehicle, reference_velocityX_m_s):
        super().__init__(vehicle)
        self.reference_velocityX = reference_velocityX_m_s

    def update(self):
        # 車両の速度を一定に保つための加速度を計算する
        self.accX_input = (self.reference_velocityX - self.vehicle.get_velocityX()) / TIME_STEP
        self.vehicle.set_accX_input(self.accX_input)