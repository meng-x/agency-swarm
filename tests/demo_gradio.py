import sys
import os

import gradio as gr
from dotenv import load_dotenv
load_dotenv()
sys.path.insert(0, '..')

from agency_swarm import set_openai_key
from agency_swarm.agency.agency import Agency
from tests.ceo.ceo import Ceo
from tests.test_agent.test_agent import TestAgent
from tests.test_agent2.test_agent2 import TestAgent2

set_openai_key(os.getenv('OPENAI_API_KEY'))

test_agent1 = TestAgent()
test_agent2 = TestAgent2()
ceo = Ceo()

agency = Agency([
    ceo,
    [ceo, test_agent1, test_agent2],
    [ceo, test_agent2],
], shared_instructions="Talk in Japanese with each other.")


agency.demo_gradio(height=700)

