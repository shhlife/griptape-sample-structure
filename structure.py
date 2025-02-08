from typing import List

import typer
from griptape.artifacts import ListArtifact, TextArtifact
from griptape.structures import Agent
from griptape.utils import GriptapeCloudStructure

app = typer.Typer(add_completion=False)


@app.command()
def run(args: List[str] = typer.Argument(...)):
    """Run the agent with a prompt."""
    with GriptapeCloudStructure() as context:
        # If you want to run a Griptape Structure, set this to True
        # otherwise, if you're just running regular Python code, set it to False
        use_structure = False

        if use_structure:
            agent = Agent()
            agent.run(args)
        else:
            # Run whatever code you want and then set the context.output with the response you want to send.
            # The output can be a string, or an artifact. In this case, we'll use a ListArtifact.
            output_artifact_msg = TextArtifact("Hello from a Griptape Cloud Structure.")
            output_artifact_prompt = TextArtifact(args)

            task_output = ListArtifact([output_artifact_msg, output_artifact_prompt])
            context.output = task_output


if __name__ == "__main__":
    app()
