class DataTransformer:
    def __init__(self, required_fields):
        self.required_fields = required_fields

    def transform(self, raw_data):
        transformed_data = []
        for item in raw_data:
            try:
                record = {
                    "Name": item.get("name"),
                    "Email": item.get("email"),
                    "Feedback": item.get("feedback"),
                    "Date Submitted": item.get("date_submitted"),
                    "Status": item.get("status", "Pending") 
                }
                if self._validate_record(record):
                    transformed_data.append(record)
                else:
                    print("Registro inválido:", item)
            except Exception as e:
                print("Error al transformar el registro:", e)
        return transformed_data

    def _validate_record(self, record):
        return all(field in record and record[field] for field in self.required_fields)

