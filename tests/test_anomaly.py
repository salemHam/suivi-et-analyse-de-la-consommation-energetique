from src.anomaly import AnomalyDetector
from datetime import datetime


def test_detect_anomaly_power():
    detector = AnomalyDetector(power_threshold_max=600)

    data = {
        "power_w": 1000,
        "temperature_c": 25,
        "gas_ppm": 200,
        "timestamp": datetime.now()
    }

    anomalies = detector.detect(data)

    assert anomalies is not None
    assert "power_w" in anomalies


def test_detect_no_anomaly():
    detector = AnomalyDetector()

    data = {
        "power_w": 500,
        "temperature_c": 25,
        "gas_ppm": 200,
        "timestamp": datetime.now()
    }

    anomalies = detector.detect(data)

    assert anomalies is None
