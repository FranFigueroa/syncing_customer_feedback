import pytest
from unittest.mock import MagicMock
from airtable import AirtableClient

@pytest.fixture
def airtable_client():
    client = AirtableClient("Feedback")
    client.table = MagicMock()
    return client

def test_insert_or_update_record_insert(airtable_client):
    record = {"Name": "John", "Email": "john@example.com"}
    airtable_client.table.all.return_value = []
    airtable_client.insert_or_update_record(record)
    airtable_client.table.create.assert_called_once_with(record)

def test_insert_or_update_record_update(airtable_client):
    record = {"Name": "John", "Email": "john@example.com"}
    airtable_client.table.all.return_value = [{"id": "rec123", "fields": {"Email": "john@example.com"}}]
    airtable_client.insert_or_update_record(record)
    airtable_client.table.update.assert_called_once_with("rec123", record)

