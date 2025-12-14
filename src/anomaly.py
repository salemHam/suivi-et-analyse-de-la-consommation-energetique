from src.const import (
    MEAN_POWER,
    STD_POWER,
    MEAN_TEMP,
    STD_TEMP,
    MEAN_GAS,
    STD_GAS
)


class AnomalyDetector:
    def __init__(
        self,
        power_threshold_max=MEAN_POWER + 2 * STD_POWER,
        power_threshold_min=MEAN_POWER - 2 * STD_POWER,
        temp_threshold_min=MEAN_TEMP - 2 * STD_TEMP,
        temp_threshold_max=MEAN_TEMP + 2 * STD_TEMP,
        gas_threshold_max=MEAN_GAS + 2 * STD_GAS,
        gas_threshold_min=MEAN_GAS - 2 * STD_GAS,
    ):
        self.power_threshold = power_threshold_max
        self.power_threshold_min = power_threshold_min
        self.temp_threshold_max = temp_threshold_max
        self.temp_threshold_min = temp_threshold_min
        self.gas_threshold_max = gas_threshold_max
        self.gas_threshold_min = gas_threshold_min

    def detect(self, data):
        anomalies = {}
        if (
            data["power_w"] > self.power_threshold
            or data["power_w"] < self.power_threshold_min
        ):
            anomalies["power_w"] = data["power_w"]
        if (
            data["temperature_c"] > self.temp_threshold_max
            or data["temperature_c"] < self.temp_threshold_min
        ):
            anomalies["temperature_c"] = data["temperature_c"]
        if (
            data["gas_ppm"] > self.gas_threshold_max
            or data["gas_ppm"] < self.gas_threshold_min
        ):
            anomalies["gas_ppm"] = data["gas_ppm"]

        if anomalies:
            anomalies["timestamp"] = data["timestamp"]
            return anomalies
        return None
