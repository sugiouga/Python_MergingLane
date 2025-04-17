import config as Config

# 車両クラスを定義する
class Vehicle:

    def __init__(self, vehicle_id, road_id, positionX_m, positionY_m, velocityX_m_s, accelerationX_m_s2, controller):
        # 車両の物理的な特性を定義する
        self.WIDTH = 1.69
        self.LENGTH = 5.25
        self.MIN_VELOCITY = 0
        self.MAX_VELOCITY = 25
        self.MIN_ACCELERATION = -3
        self.MAX_ACCELERATION = 2
        self.TIME_STEP = Config.TIME_STEP

        # IDを設定する
        self.vehicle_id = vehicle_id
        self.road_id = road_id

        # 車両の初期位置、速度、加速度を設定する
        # 車両の位置は絶対座標を表す
        self.positionX = positionX_m
        self.positionY = positionY_m
        self.velocityX = velocityX_m_s
        self.accelerationX = accelerationX_m_s2
        self.jerkX = 0
        self.accX_input = 0

        # 車両の制御器を設定する
        self.controller = controller

    # 車両の情報を取得するメソッド
    def get_vehicle_id(self):
        return self.vehicle_id

    def get_road_id(self):
        return self.road_id

    def get_positionX(self):
        return self.positionX

    def get_positionY(self):
        return self.positionY

    def get_velocityX(self):
        return self.velocityX

    def get_accelerationX(self):
        return self.accelerationX

    def get_jerkX(self):
        return self.jerkX

    def get_accX_input(self):
        return self.accX_input

    def get_controller(self):
        return self.controller

    # 車両の情報を変更するメソッド
    def set_road_id(self, road_id):
        self.road_id = road_id

    def set_positionX(self, positionX_m):
        self.positionX = positionX_m

    def set_positionY(self, positionY_m):
        self.positionY = positionY_m

    def set_accX_input(self, accX_input):
        self.accX_input = accX_input

    def set_controller(self, controller):
        self.controller = controller

    # 車両の位置･速度を更新するメソッド
    def update_vehicle(self):
        # 制御器から加速度入力を受け取る
        if self.controller is not None:
            self.controller.update()

        # 車両の加速度入力を制限する
        if self.accX_input < self.MIN_ACCELERATION:
            self.accX_input = self.MIN_ACCELERATION
        elif self.accX_input > self.MAX_ACCELERATION:
            self.accX_input = self.MAX_ACCELERATION

        # ジャークを計算する
        self.jerkX = (self.accelerationX - self.accX_input) / self.TIME_STEP
        # 加速度入力を受け取る
        self.accelerationX = self.accX_input

        # 車両の位置･速度を更新する
        self.positionX += self.velocityX * self.TIME_STEP + 0.5 * self.accelerationX * (self.TIME_STEP ** 2)
        self.velocityX += self.accelerationX * self.TIME_STEP

        # 車両の位置･速度を制限する
        if self.velocityX < self.MIN_VELOCITY:
            self.velocityX = self.MIN_VELOCITY
        elif self.velocityX > self.MAX_VELOCITY:
            self.velocityX = self.MAX_VELOCITY
