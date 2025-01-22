import pytest
from data_fetcher import DataFetcher

@pytest.fixture
def fetcher():
    return DataFetcher("https://jsonplaceholder.typicode.com/posts")

def test_fetch_data_success(fetcher):
    data = fetcher.fetch_data()
    assert len(data) > 0
    assert isinstance(data, list)

def test_fetch_data_invalid_url():
    invalid_fetcher = DataFetcher("https://invalid-url.com")
    data = invalid_fetcher.fetch_data()
    assert data == []

