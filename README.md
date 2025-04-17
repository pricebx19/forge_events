# Forge Events

[![PyPI version](https://badge.fury.io/py/forge-events.svg)](https://badge.fury.io/py/forge-events)
[![Build Status](https://github.com/forge-framework/forge_events/actions/workflows/tests.yml/badge.svg)](https://github.com/forge-framework/forge_events/actions)
[![Coverage](https://codecov.io/gh/forge-framework/forge_events/branch/main/graph/badge.svg)](https://codecov.io/gh/forge-framework/forge_events)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Event-driven internals Explain the purpose and responsibility of this package within the larger Forge framework.

## Installation

```bash
pip install forge-events
# or with Poetry
poetry add forge-events
```

## Features

- Feature 1: Description
- Feature 2: Description
- Feature 3: Description

## Usage

```python
from forge_events import SomeClass

# Example code
instance = SomeClass()
result = instance.do_something()
```

## Architecture

This package follows the principles of Clean Architecture and Domain-Driven Design:

- Domain logic is isolated from infrastructure concerns
- Interfaces (Protocols) are used for dependency injection
- Each file contains a single class or function
- Full type annotations throughout the codebase

## Development

### Setting up the development environment

```bash
# Clone the repository
git clone https://github.com/forge-framework/forge_events.git
cd forge_events

# Install dependencies with Poetry
poetry install

# Activate the virtual environment
poetry shell
```

### Running tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=forge_events

# Run specific tests
pytest tests/test_specific_file.py
```

### Code quality tools

```bash
# Format code with Black
black forge_events tests

# Check imports with isort
isort forge_events tests

# Run linter (Ruff)
ruff check forge_events tests

# Run type checking with mypy
mypy forge_events
```

## License

MIT
