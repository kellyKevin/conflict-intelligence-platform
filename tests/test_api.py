import pytest
from httpx import ASGITransport, AsyncClient
import sys
import os

# Add backend to path
sys.path.append(os.path.abspath("backend"))
from main import app

@pytest.mark.asyncio
async def test_ews_risk_index():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/ews/risk-index?region=Sudan")
    assert response.status_code == 200
    assert response.json()["region"] == "Sudan"
    assert "current_risk_score" in response.json()

@pytest.mark.asyncio
async def test_pta_treaty_analysis():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/pta/treaty-analysis?text=The parties shall refrain from force.")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert "label" in response.json()[0]

@pytest.mark.asyncio
async def test_chm_counterfactual():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/chm/counterfactual-query?treatment=funding&outcome=stability")
    assert response.status_code == 200
    assert "effect" in response.json()

@pytest.mark.asyncio
async def test_efaw_ethical_score():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/efaw/ethical-score?autonomy=0.8&confidence=0.9&density=0.5&proportionality=0.4")
    assert response.status_code == 200
    assert "risk_score" in response.json()
