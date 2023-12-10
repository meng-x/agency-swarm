from agency_swarm.agents import Agent


class Consultant(Agent):
    def __init__(self):
        super().__init__(
            name="Consultant",
            description="Aflac Life Insurance Consultant. Responsible for client communication, task planning and management.",
            instructions="./instructions.md",
            files_folder="./files"
        )
