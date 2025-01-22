from pyairtable import Table
import os
from dotenv import load_dotenv

load_dotenv()

# Variables
API_KEY = os.getenv("AIRTABLE_API_KEY")
BASE_ID = os.getenv("BASE_ID")
TABLE_NAME = "Feedback"  

class AirtableClient:
    def __init__(self, table_name):
        self.table = Table(API_KEY, BASE_ID, table_name)

    def fetch_records(self):
        try:
            return self.table.all()
        except AirtableApiError as e:
            print(f"Error de API al obtener registros: {e}")
            return []
        except Exception as e:
            print(f"Error desconocido al obtener registros: {e}")
            return []

    def insert_or_update_record(self, record):
        try:
            existing_records = self.table.all()
            for existing in existing_records:
                if existing["fields"].get("Email") == record.get("Email"):
                    self.table.update(existing["id"], record)
                    print(f"Registro actualizado: {record}")
                    return
            self.table.create(record)
            print(f"Registro insertado: {record}")
        except AirtableApiError as e:
            print(f"Error de API al insertar o actualizar registros: {e}")
        except Exception as e:
            print(f"Error desconocido al insertar o actualizar registros: {e}")

# Testing Connection
TABLE_NAME = "Feedback"
FIELDS = ["Name", "Email", "Feedback", "Date Submitted", "Status"]
print("Conexión exitosa:", table.all())

