import os

import click
from griptape.drivers import GriptapeCloudEventListenerDriver, OpenAiChatPromptDriver
from griptape.events import EventBus, EventListener
from griptape.structures import Agent
from griptape.tools import DateTimeTool


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
        # If not, we need to load the .env file ourselves
        from dotenv import load_dotenv

        load_dotenv()


@click.command()
@click.argument("prompt")
@click.option(
    "--model",
    "-m",
    type=click.Choice(["gpt-4o", "gpt-3.5-turbo", "gpt-4o-mini"], case_sensitive=False),
    default="gpt-4o",
    show_default=True,
    help="The model to use",
)
def run(prompt, model):
    """Runs the agent with the given prompt and optional model selection."""
    setup_cloud_listener()

    agent = Agent(
        prompt_driver=OpenAiChatPromptDriver(model=model), tools=[DateTimeTool()]
    )
    agent.run(prompt)


if __name__ == "__main__":
    run()
