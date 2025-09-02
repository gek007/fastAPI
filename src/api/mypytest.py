import api.mypytest as mypytest
from httpx import AsyncClient
from fastapi import FastAPI
from src.api.hotels import router

app = FastAPI()
app.include_router(router)

@mypytest.mark.asyncio
async def test_get_hotels():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/hotels")
    assert response.status_code == 200

@mypytest.mark.asyncio
async def test_get_hotel_by_id():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/hotels/1")
    assert response.status_code == 200 or response.status_code == 404

@mypytest.mark.asyncio
async def test_create_hotel():
    hotel_data = {
        "title": "Test Hotel",
        "name": "test_hotel",
        "location": "Test Location"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/hotels", json=hotel_data)
    assert response.status_code == 200
    assert response.json()["status"] == "OK"

@mypytest.mark.asyncio
async def test_edit_hotel():
    hotel_data = {
        "title": "Updated Hotel",
        "name": "updated_hotel",
        "location": "Updated Location"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.put("/hotels/1", json=hotel_data)
    assert response.status_code == 200
    assert response.json()["status"] == "OK"

@mypytest.mark.asyncio
async def test_partially_edit_hotel():
    hotel_data = {
        "title": "Partially Updated Hotel"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.patch("/hotels/1", json=hotel_data)
    assert response.status_code == 200
    assert response.json()["status"] == "OK"

@mypytest.mark.asyncio
async def test_delete_hotel():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/hotels/1")
    assert response.status_code == 200
    assert response.json()["status"] == "OK"