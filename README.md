# Griptape Sample Structure Template

This is a simple example structure template that can be used to run a Griptape Agent or publish the output from generic Python Code.

## How it works

In `structure.py` you can set the `use_structure` parameter to `True` or `False`.

If `True`, it will utilize a Griptape Structure and the results of the structure run will automatically be published.

```python
    with GriptapeCloudStructure() as context:
        if use_structure:
            # Run the agent with the provided arguments
            agent = Agent()
            agent.run(args)
```

If `False`, you can run any kind of Python code. When ready to publish the results, set `context.output` to whatever you want the output to be.


```python
    with GriptapeCloudStructure() as context:
        if not use_structure:
            # Run whatever code you want and then set the context.output with the response you want to send.
            # The output can be a string, an Artifact, or a ListArtifact
            output_msg = f"You sent: {args}"

            # Use context.output to publish the output message
            context.output = output_msg
```

## How to use it

Choose the **Use This Template** button to create a new GitHub repository with this template.

## Requirements

The structure requires two API keys:

* [Open AI Key](https://platform.openai.com/api-keys)
* [Griptape Cloud Key](https://cloud.griptape.ai/configuration/api-keys)
    > ℹ️ _Note_: The Griptape Cloud API key should be automatically created for you now. This is a new feature.

## Configuration

Save the following key in your `.env` if running locally, or add it to the structure if running in Griptape Cloud.

```.env
OPENAI_API_KEY=<encrypted_value> # Fill in with your own key
```
