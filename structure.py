import os
import sys

from dotenv import load_dotenv

from griptape.structures import Agent
from griptape.events import EventListener, EventBus
from griptape.drivers import GriptapeCloudEventListenerDriver

def setup_cloud_listener():
    api_key = os.environ.get("GT_CLOUD_API_KEY")
    if not api_key:
        raise ValueError("GT_CLOUD_API_KEY environment variable is required")
    
    EventBus.add_event_listeners([
        EventListener(
            event_listener_driver=GriptapeCloudEventListenerDriver(api_key=api_key)
        )
    ])

if __name__ == "__main__":
    input = sys.argv[1]

    if "GT_CLOUD_STRUCTURE_RUN_ID" in os.environ:
        setup_cloud_listener()
    else:
        load_dotenv()

    agent = Agent()
    result = agent.run(input)
