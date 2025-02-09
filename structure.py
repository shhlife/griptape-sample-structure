from typing import List

import typer
from griptape.artifacts import TextArtifact
from griptape.structures import Agent
from griptape.utils import GriptapeCloudStructure

app = typer.Typer(add_completion=False)

# If you want to run a Griptape Structure, set this to True
# otherwise, if you're just running regular Python code, set it to False
use_structure = True


@app.command()
def run(args: List[str] = typer.Argument(...)):
    """Run the agent with a prompt."""
    with GriptapeCloudStructure() as context:
        if use_structure:
            # Run the agent with the provided arguments
            agent = Agent()
            agent.run(args)
        else:
            # Run whatever code you want and then set the context.output with the response you want to send.
            # The output must be a TextArtifact or ListArtifact
            output_msg = TextArtifact(f"You sent: {args}")

            # Use context.output to publish the output message
            context.output = output_msg


if __name__ == "__main__":
    app()
