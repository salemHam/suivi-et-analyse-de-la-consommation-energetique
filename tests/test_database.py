from unittest.mock import MagicMock
from src.database import saveToMongoDB


def test_save_to_mongodb():
    mock_client = MagicMock()
    mock_collection = MagicMock()
    mock_client.__getitem__.return_value.__getitem__.return_value = mock_collection

    mock_collection.insert_one.return_value.inserted_id = "fake_id"

    db = saveToMongoDB(mock_client)
    record_id = db.save({"test": "data"}, anomalies=False)

    assert record_id == "fake_id"
    mock_collection.insert_one.assert_called_once()
