from airtable import AirtableClient
from data_fetcher import DataFetcher
from data_transformer import DataTransformer

# Configuración general
API_URL = "https://example.com/api/feedback"
TABLE_NAME = "Feedback" 
REQUIRED_FIELDS = ["Name", "Email", "Feedback", "Date Submitted", "Status"]

def main():
    # Modules
    fetcher = DataFetcher(API_URL)
    transformer = DataTransformer(REQUIRED_FIELDS)
    airtable_client = AirtableClient(TABLE_NAME)

    # Step 1: Get Data
    print("Obteniendo datos del sistema externo...")
    raw_data = fetcher.fetch_data()
    if not raw_data:
        print("No se obtuvieron datos del sistema externo. Finalizando.")
        return

    # Step 2: Transform data
    print("Transformando datos...")
    transformed_data = transformer.transform(raw_data)
    if not transformed_data:
        print("No se pudieron transformar los datos. Finalizando.")
        return

    # Step 3: Instert data
    print("Insertando o actualizando registros en Airtable...")
    for record in transformed_data:
        airtable_client.insert_or_update_record(record)

    print("Proceso completado con éxito.")

if __name__ == "__main__":
    main()

