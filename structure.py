import os

import typer
from griptape.artifacts import ListArtifact, TextArtifact
from griptape.drivers import GriptapeCloudEventListenerDriver
from griptape.events import (
    EventBus,
    EventListener,
    FinishStructureRunEvent,
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
def run(prompt: str):
    """Run the agent with a prompt."""
    agent = Agent()
    agent.run(prompt)
    setup_cloud_listener()

    print("Publishing final event...")
    artifacts = ListArtifact([agent.output])  # listy mc listerson
    print(artifacts)
    task_input = TextArtifact(value=None)
    done_event = FinishStructureRunEvent(
        output_task_input=task_input, output_task_output=artifacts
    )

    EventBus.publish_event(done_event, flush=True)


if __name__ == "__main__":
    app()
