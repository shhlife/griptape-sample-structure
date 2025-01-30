import os
from enum import Enum

import typer
from griptape.drivers import GriptapeCloudEventListenerDriver, OpenAiChatPromptDriver
from griptape.events import (
    EventBus,
    EventListener,
    StartActionsSubtaskEvent,
)
from griptape.structures import Agent

def setup_cloud_listener():
    # Are we running in a managed environment?
    if "GT_CLOUD_STRUCTURE_RUN_ID" in os.environ:
        # If so, the runtime takes care of loading the .env file
        EventBus.add_event_listener(
            EventListener(
                event_listener_driver=GriptapeCloudEventListenerDriver(),
            )
        )
    else:
        EventBus.add_event_listener(
            EventListener(
                event_types=[StartActionsSubtaskEvent],
            )
        )
        # If not, we need to load the .env file ourselves
        from dotenv import load_dotenv

        load_dotenv()


app = typer.Typer(add_completion=False)


@app.command()
def run(
    prompt: str
):
    """Run the agent with a prompt."""
    setup_cloud_listener()
    Agent().run(prompt)


if __name__ == "__main__":
    app()
