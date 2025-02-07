import json
from app.schemas.scenario import Scenario
from app.schemas.client import Client


async def migrate_initial_data(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    scenario_data = data.get("Scenario", [])
    client_data = data.get("Client", [])

    for scenario in scenario_data:
        existing = await Scenario.find_one(Scenario.name == scenario["name"])
        if not existing:
            new_scenario = Scenario(**scenario)
            await new_scenario.insert()
            print(f"Scenario has been added {scenario['name']}")

    for client in client_data:
        existing = await Client.find_one(Client.name == client["name"])
        if not existing:
            new_client = Client(**client)
            await new_client.insert()
            print(f"New client [{client['name']}] has been added into DB")


