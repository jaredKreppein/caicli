# Contributing

## Setup

#### Install Python and Dependencies

This repo uses Python `3.11.4`.

```bash
# install pyenv or use whatever version manager you prefer
brew install pyenv

# install poetry
curl -sSL https://install.python-poetry.org | python3 -

# install dependencies
pyenv install
poetry install
```

#### Linting & Formatting

Uses [Ruff](https://github.com/astral-sh/ruff), a Python linter/formatter written in Rust.

```bash
# run the formatter on all files
poetry run ruff format .

# check all files, add --fix to autofix issues
poetry run ruff check .
```

#### Testing & Coverage

```bash
poetry run pytest

# include missing
poetry run pytest --cov-report term-missing
```

#### Running the CLI

```bash
poetry run main <args>
```
