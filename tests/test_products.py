from fastapi import status
from fastapi.testclient import TestClient

from app.const import (
    PRODUCTS_URL
)
from app.main import app


client = TestClient(app)


def test_get_product(headers):

    response = client.get("/" + PRODUCTS_URL + "/1", headers=headers)
    schema = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert schema["id"] == 1


def test_get_products(headers):
    url = "/" + PRODUCTS_URL
    response = client.get(url, headers=headers)
    schema = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(schema) > 0
