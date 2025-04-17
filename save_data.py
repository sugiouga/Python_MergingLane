import csv
import os

class SaveData:
    def __init__(self, simulation):
        self.simulation = simulation  # シミュレーションデータを保持

    def save_simulation_data(self, result_dir, simulation_id):
        """
        シミュレーションごとにフォルダを作成し、各ビークルのデータをCSVファイルに保存する。
        :param result_dir: 結果を保存するディレクトリ
        :param simulation_id: シミュレーションの識別子
        """
        # シミュレーションごとのフォルダを作成
        simulation_dir = os.path.join(result_dir, f"simulation_{simulation_id}")
        os.makedirs(simulation_dir, exist_ok=True)

        for vehicle in self.simulation.get_all_vehicles():  # 全ビークルデータを取得
            # 各ビークルごとにファイルを作成
            filename = os.path.join(simulation_dir, f'vehicle_{vehicle.vehicle_id}.csv')

            # ヘッダー
            headers = ['road_id', 'positionX', 'positionY', 'velocityX', 'accelerationX', 'jarkX', 'Simulation_time']

            # データ収集
            vehicle_data = []
            for record in vehicle.get_records():  # 各ビークルの履歴データを取得
                vehicle_data.append([
                    record.road_id,
                    record.positionX,
                    record.positionY,
                    record.velocityX,
                    record.accelerationX,
                    record.jarkX,
                    record.simulation_time  # シミュレーション時間を追加
                ])

            # CSVファイルに書き込み
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)  # ヘッダーを書き込む
                writer.writerows(vehicle_data)  # ビークルデータを書き込む