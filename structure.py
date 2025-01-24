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
from griptape.tools import DateTimeTool


class Model(str, Enum):
    GPT4 = "gpt-4o"
    GPT35 = "gpt-3.5-turbo"
    GPT4_MINI = "gpt-4o-mini"


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
    prompt: str,
    model: Model = typer.Option(Model.GPT4, "--model", "-m", help="The model to use"),
):
    """Run the agent with a prompt."""
    setup_cloud_listener()
    Agent(
        prompt_driver=OpenAiChatPromptDriver(model=model, stream=True),
        tools=[DateTimeTool()],
    ).run(prompt)


if __name__ == "__main__":
    app()
