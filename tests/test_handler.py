# external imports
import pytest
from fastapi.testclient import TestClient

# internal imports
from src.app import app


# test the root route
@pytest.fixture()
def async_client() -> TestClient:
    return TestClient(app)


@pytest.mark.asyncio()
async def test_root_get(async_client: TestClient) -> None:
    response = async_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.asyncio()
async def test_root_post(async_client: TestClient) -> None:
    response = async_client.post("/events", json={"content": "Hello World"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
