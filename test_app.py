import pytest
import httpx
from fastapi.testclient import TestClient
from FastAPI_backend.main import app, ModelInput


client = TestClient(app)

#successful prediction
def test_successful_prediction():
    test_data = {
        "temp": 25.0,
        "Ws": 13.0,
        "Rain": 2.5,
        "FFMC": 28.6,
        "DMC": 1.3,
        "ISI": 0.0
    }
    response = client.post("/prediction", json=test_data)
    assert response.status_code == 200
    assert response.json()["prediction value"] in [0, 1]

#failed prediction due to missing data
@pytest.mark.asyncio
async def test_smoke():
    async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/smoke")
        assert response.status_code == 200
        assert response.json() == {"status": "OK"}


