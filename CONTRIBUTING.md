# Contributing

## Setup

#### Install Python and Dependencies

This repo uses Python `3.11.4`.

```bash
# install pyenv or use whatever version manager you prefer
brew install pyenv
pyenv install

# install poetry
curl -sSL https://install.python-poetry.org | python3 -

# install dependencies
pyenv install
poetry install
```

Formatting

```bash
# optionally add --fix for ruff to fix for you
poetry run ruff format .
poetry run ruff check .
```

Running the CLI

```bash
poetry run python src/cli.py <args>
```

Testing

```bash
poetry run pytest
```
