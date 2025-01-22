import pytest
from data_transformer import DataTransformer

@pytest.fixture
def transformer():
    required_fields = ["Name", "Email", "Feedback", "Date Submitted", "Status"]
    return DataTransformer(required_fields)

def test_transform_valid_data(transformer):
    raw_data = [
        {"name": "John", "email": "john@example.com", "feedback": "Great!", "date_submitted": "2025-01-21"}
    ]
    transformed_data = transformer.transform(raw_data)
    assert len(transformed_data) == 1
    assert transformed_data[0]["Name"] == "John"

def test_transform_invalid_data(transformer):
    raw_data = [{"name": "John"}]
    transformed_data = transformer.transform(raw_data)
    assert len(transformed_data) == 0

