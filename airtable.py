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
        except Exception as e:
            print("Error al obtener los registros:", e)
            return []

    def insert_record(self, record):
        try:
            return self.table.create(record)
        except Exception as e:
            print("Error al insertar el registro:", e)
            return None

# Testing Connection
table = Table(API_KEY, BASE_ID, TABLE_NAME)
print("Conexión exitosa:", table.all())

