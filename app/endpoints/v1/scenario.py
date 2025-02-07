from fastapi import APIRouter, HTTPException
from app.schemas.scenario import Scenario
from app.services.scenario import ScenarioService


router = APIRouter(tags=["Request settings"])


@router.get('/scenarios')
async def get_scenarios() -> list[Scenario]:
    try:
        service = ScenarioService()
        scenarios = await service.read_many()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    return scenarios


@router.get('/scenarios/{scenario_id}')
async def get_scenario(scenario_id: str) -> Scenario:
    try:
        service = ScenarioService()
        scenario = await service.read_one(scenario_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    return scenario


@router.post('/scenarios', response_model=Scenario)
async def create_scenario(scenario_data: Scenario):
    try:
        service = ScenarioService()
        scenario = await service.create_scenario(scenario_data=scenario_data.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    return scenario
