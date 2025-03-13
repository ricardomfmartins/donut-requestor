# Donut requestor

This repository stores the definition of an API to buy donuts.
To buy a donut box, you need to state what is size of the box of donuts you want to buy and then you can select the donut flavours you want to add to it.

## Setup

Install uv (Python package manager)
[uv installation docs](https://docs.astral.sh/uv/getting-started/installation/)

```bash
uv venv .venv
````

Activate venv with the command line given by uv

```bash
uv sync
```

## Tests

Run the command line
```bash
uv run pytest tests/unit
```
