from airtable import AirtableClient
from data_fetcher import DataFetcher
from data_transformer import dataTransformer

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


raw_data = [
    {"name": "John Doe", "email": "john@example.com", "feedback": "Great service!", "date_submitted": "2025-01-20"},
    {"name": "Jane Smith", "email": "jane@example.com", "feedback": "Could be better", "date_submitted": "2025-01-19"}
]
REQUIRED_FIELDS = ["Name", "Email", "Feedback", "Date Submitted", "Status"]

transformer = DataTransformer(REQUIRED_FIELDS)
transformed_data = transformer.transform(raw_data)
print("Datos transformados:", transformed_data)

