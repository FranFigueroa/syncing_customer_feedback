# Airtable Feedback Sync

Este proyecto sincroniza datos de feedback de clientes desde un sistema externo a Airtable, permitiendo una gestión eficiente y centralizada de los registros para su análisis y seguimiento.

## Funcionalidades
- **Obtención de datos externos:** Conexión a una API externa para extraer datos de feedback.
- **Transformación de datos:** Adaptación de los datos al formato requerido por Airtable.
- **Sincronización con Airtable:** Inserción o actualización de registros en una tabla específica.
- **Manejo de errores:** Gestión robusta de errores en la interacción con la API externa y Airtable.
- **Pruebas unitarias e integración:** Cobertura completa de los módulos principales para garantizar la confiabilidad del sistema.

## Requisitos
- Python 3.8 o superior.
- Cuenta activa en Airtable con una API Key.
- Conexión a un sistema externo que proporcione los datos en formato JSON.

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/franfigueroa/syncing_customer_feedback.git
   cd syncing_customer_feedback.git
```
2. Crear y activar entorno virtual
```bash
python -m venv venv
source venv/bin/activate  
venv\Scripts\activate     
```
3. Intalar dependencias

pip install -r requirements.txt

4. Configurar variables de entorno

AIRTABLE_API_KEY=your_airtable_api_key
BASE_ID=your_base_id

## Uso
```bash
python src/main.py
```

## Estructura del Proyecto

syncing_customer_feedback/
├── src/
│   ├── airtable.py          
│   ├── data_fetcher.py      
│   ├── data_transformer.py  
│   └── main.py              
├── tests
│   ├── test_airtable.py     
│   ├── test_data_fetcher.py 
│   └── test_data_transformer.py 
├── .env                     
├── requirements.txt         
└── README.md                



```bash
pytest tests/
```

## Mejoras futuras
Implementar un sistema de notificaciones para errores críticos.
Añadir soporte para múltiples tablas y configuraciones dinámicas.
Optimizar el rendimiento en operaciones con grandes volúmenes de datos.

## Licencia

Este proyecto está licenciado bajo la MIT License.

