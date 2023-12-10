from agency_swarm.agents import Agent


class Expert(Agent):
    def __init__(self):
        super().__init__(
            name="Expert",
            description="Aflac Life Insurance Expert in personalized insurance advice with web references. Understands everything aspect of Aflac life insurance.",
            instructions="./instructions.md",
            files_folder="./files"
        )
