from datetime import datetime
import random
import time
# Constantes pour la simulation
from src.const import (
    VOLTAGE,
    MEAN_POWER,
    STD_POWER,
    MEAN_TEMP,
    STD_TEMP,
    MEAN_GAS,
    STD_GAS,
    BILLING_PERIOD_DAYS
)


class SimpleEnergySensor:
    def __init__(
        self,
        voltage=VOLTAGE,
        mean_power=MEAN_POWER,
        std_power=STD_POWER,
        mean_temp=MEAN_TEMP,
        std_temp=STD_TEMP,
        mean_gas=MEAN_GAS,
        std_gas=STD_GAS,
        billing_period_days=BILLING_PERIOD_DAYS
    ):
        # Énergie
        self.voltage = voltage
        self.mean_power = mean_power
        self.std_power = std_power

        # Température
        self.mean_temp = mean_temp
        self.std_temp = std_temp

        # Gaz (ppm)
        self.mean_gas = mean_gas
        self.std_gas = std_gas

        # Facturation
        self.billing_period_days = billing_period_days

        self.energy_kwh = 0.0
        self.last_time = time.time()
        self.period_start_time = time.time()

        # Historique des périodes
        self.billing_history = []

    def _reset_if_needed(self, now):
        period_seconds = self.billing_period_days * 24 * 3600
        if now - self.period_start_time >= period_seconds:
            self.billing_history.append({
                "energy_kwh": round(self.energy_kwh, 3),
                "date_start": datetime.fromtimestamp(self.period_start_time),
                "date_end": datetime.fromtimestamp(now)
            })
            self.energy_kwh = 0.0
            self.period_start_time = now

    def read(self):
        now = time.time()
        delta_h = (now - self.last_time) / 3600
        self.last_time = now

        # Reset trimestriel si nécessaire
        self._reset_if_needed(now)

        # Puissance
        power_w = max(random.gauss(self.mean_power, self.std_power), 0)

        # Courant
        current_a = power_w / self.voltage

        # Énergie cumulée
        self.energy_kwh += (power_w * delta_h) / 1000

        # Température
        temperature_c = random.gauss(self.mean_temp, self.std_temp)

        # Gaz (ppm)
        gas_ppm = max(random.gauss(self.mean_gas, self.std_gas), 0)

        return {
            "power_w": round(power_w, 2),
            "current_a": round(current_a, 3),
            "energy_kwh": round(self.energy_kwh, 5),
            "temperature_c": round(temperature_c, 2),
            "gas_ppm": round(gas_ppm, 1),
            "timestamp": datetime.fromtimestamp(now)
        }
