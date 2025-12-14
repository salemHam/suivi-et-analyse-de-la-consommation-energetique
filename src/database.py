
class saveToMongoDB:
    def __init__(self, db_client, db_name="energy_monitoring", collection_name="sensor_data", clear_db=False):
        self.db = db_client[db_name]
        self.collection = self.db[collection_name]
        if clear_db:
            self.collection.delete_many({})

    def save(self, data, anomalies=False):
        data["anomalies"] = anomalies
        result = self.collection.insert_one(data)
        return result.inserted_id

    def save_history(self, history):
        if history is None or len(history) == 0:
            return []
        # en mettant date debut comme id
        history_with_ids = [{**record, "_id": record["date_start"]}
                            for record in history]
        result = self.db["billing_history"].insert_many(history_with_ids)
        return result.inserted_ids

    def get_records(self, filter=None):
        if filter is None:
            filter = {}
        return list(self.collection.find(filter))
