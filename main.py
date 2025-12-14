
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from env import uri
import time

from src.sensor import SimpleEnergySensor
from src.database import saveToMongoDB
from src.anomaly import AnomalyDetector
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

if __name__ == "__main__":
    sensor = SimpleEnergySensor()
    db_saver = saveToMongoDB(client, clear_db=True)
    anomaly_detector = AnomalyDetector()

    for _ in range(10):  # Simuler 10 lectures
        data = sensor.read()

        # Détection d'anomalies
        anomalies = anomaly_detector.detect(data)
        if anomalies:
            # afficher en rouge les anomalies détectées
            print("\033[91mAnomalies détectées:", anomalies, "\033[0m")

        # Sauvegarde dans MongoDB
        record_id = db_saver.save(data, anomalies=bool(anomalies))
        # afficher en vert l'id du record sauvegardé
        print(f"\033[92m Données sauvegardées avec l'ID: {record_id} \033[0m")
        time.sleep(1)  # Pause d'une seconde entre les lectures

    filter = {"anomalies": {"$ne": False}}
    record_anomalies = db_saver.get_records(filter)
    print(f"Nombre total d'enregistrements avec anomalies: {len(record_anomalies)}")
    for record in record_anomalies:
        print(record)

    history = db_saver.save_history(sensor.billing_history)
    print(f"Historique de facturation sauvegardé avec les IDs: {history}")
