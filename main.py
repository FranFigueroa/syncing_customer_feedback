from airtable import AirtableClient
from data_fetcher import DataFetcher

# Client
client = AirtableClient("Feedback")

# Tesing GET Registers
records = client.fetch_records()
for record in records:
    print(record["fields"])

# Testing new record
new_record = {"Name": "John Doe", "Feedback": "Great service!"}
response = client.insert_record(new_record)
print("Registro insertado:", response)

# Testing Data Fetcher module
API_URL = "https://example.com/api/feedback"
fetcher = DataFetcher(API_URL)

# Obtener datos
external_data = fetcher.fetch_data()
print("Datos obtenidos:", external_data)

