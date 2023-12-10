import sys
import os

import gradio as gr
from dotenv import load_dotenv
load_dotenv()
sys.path.insert(0, '..')

from agency_swarm import set_openai_key
from agency_swarm.agency.agency import Agency
from Aflac.consultant.consultant import Consultant
from Aflac.assistant.assistant import Assistant
from Aflac.expert.expert import Expert

set_openai_key(os.getenv('OPENAI_API_KEY'))

consultant = Consultant()
assistant = Assistant()
expert = Expert()

agency = Agency([
    consultant,
    [consultant, expert],
    [consultant, assistant]
], shared_instructions="You are a member of an agency which provides life insurance guidance to the user. The agency has 3 agents includeing consultant, insurance expert and assistant.")


agency.demo_gradio(height=700)

