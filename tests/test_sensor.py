from src.sensor import SimpleEnergySensor


def test_sensor_read_returns_expected_keys():
    sensor = SimpleEnergySensor()
    data = sensor.read()

    assert "power_w" in data
    assert "current_a" in data
    assert "energy_kwh" in data
    assert "temperature_c" in data
    assert "gas_ppm" in data
    assert "timestamp" in data


def test_sensor_values_are_positive():
    sensor = SimpleEnergySensor()
    data = sensor.read()

    assert data["power_w"] >= 0
    assert data["current_a"] >= 0
    assert data["energy_kwh"] >= 0
    assert data["gas_ppm"] >= 0
