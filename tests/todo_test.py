from fastapi import status
import httpx
import pytest

BASE_URL = "http://localhost:8000"


@pytest.mark.asyncio
async def test_create_todo():
    data = {"name": "Test", "completed": True, "day": 2}

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/create-todo/", json=data)
        assert response.status_code == status.HTTP_200_OK
        assert "name" in response.json()


@pytest.mark.asyncio
async def test_get_all_todo():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/get-all-todo/")
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_get_todo():
    id = 15
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/get-todo/{id}/")
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.asyncio
async def test_update_todo_status():
    data = {
        "id": 14,
        "completed": True
    }
    async with httpx.AsyncClient() as client:
        response = await client.patch(f"{BASE_URL}/update-todo-status/", json=data)
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.asyncio
async def test_delete_todo():
    id = 18
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}/delete-todo/{id}/")
        assert response.status_code == status.HTTP_200_OK

