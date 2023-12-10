from agency_swarm.agents import Agent


class Assistant(Agent):
    def __init__(self):
        super().__init__(
            name="Assistant",
            description="Assistant Agent that can fetch and analyze user profile information in life insurance context",
            instructions="./instructions.md",
            files_folder="./files"
        )
