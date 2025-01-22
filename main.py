from airtable import AirtableClient

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

