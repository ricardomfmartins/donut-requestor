# Donut requestor

This repository stores the definition of an API to buy donuts.
To buy a donut box, you need to state what is size of the box of donuts you want to buy and then you can select the donut flavours you want to add to it.

## Setup

Install uv (Python package manager)
[uv installation docs](https://docs.astral.sh/uv/getting-started/installation/)

```bash
uv sync
````

Activate venv with the command line given by uv


## Tests

Run the command line
```bash
uv run pytest tests/unit
```


## Run API

```bash
uvicorn donut_requestor.main:app --reload
```

Test the API

```bash
curl --request POST --url http://127.0.0.1:8000/donuts \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.3.1' \
  --data '{"boxSize": 2,"donuts": [{"flavour": "choco"},{"flavour": "vanilla"}]}'
```
