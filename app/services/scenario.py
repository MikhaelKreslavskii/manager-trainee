from typing import Any
from app.schemas.scenario import Scenario


class ScenarioService:
    async def create_scenario(self, scenario_data: dict) -> Scenario:
        scenario = Scenario(**scenario_data)
        await scenario.insert()
        return scenario

    async def read_one(self, scenario_id: str) -> Scenario:
        scenario = await Scenario.get(document_id=scenario_id)
        return scenario

    async def read_many(self, **kwargs: Any) -> list[Scenario]:
        scenarios = await Scenario.find_all().to_list()
        return scenarios
