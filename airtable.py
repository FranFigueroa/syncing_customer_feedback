from pyairtable import Table
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Variables
API_KEY = os.getenv("AIRTABLE_API_KEY")
BASE_ID = os.getenv("BASE_ID")
TABLE_NAME = "Feedback"  

# Probar conexión
table = Table(API_KEY, BASE_ID, TABLE_NAME)
print("Conexión exitosa:", table.all())

