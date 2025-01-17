import os
import sys

from dotenv import load_dotenv

from griptape.structures import Agent

input = sys.argv[1]

agent = Agent
agent.run(input)
