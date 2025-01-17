import os
import sys

from dotenv import load_dotenv

from griptape.structures import Agent
from griptape.events import EventListener, EventBus


def is_running_in_managed_environment() -> bool:
    return "GT_CLOUD_STRUCTURE_RUN_ID" in os.environ

if __name__ == "__main__":
  input = sys.argv[1]

  if is_running_in_managed_environment():
    event_driver = GriptapeCloudEventListenerDriver(api_key=get_listener_api_key())
    EventBus.add_event_listeners(
        [
            EventListener(
                # By default, GriptapeCloudEventListenerDriver uses the api key provided
                # in the GT_CLOUD_API_KEY environment variable.
                event_listener_driver=event_driver,
            ),
        ]
    )
  else:
      load_dotenv()
  agent = Agent()
  result = agent.run(input)
