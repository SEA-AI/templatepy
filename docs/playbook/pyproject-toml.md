# pyproject.toml

## What is pyproject.toml?

`pyproject.toml` is a standardized configuration file for Python projects, introduced in [PEP 517](https://peps.python.org/pep-0517/) and [PEP 518](https://peps.python.org/pep-0518/). It's designed to replace multiple configuration files (like `setup.py`, `setup.cfg`, `MANIFEST.in`) with a single, unified configuration file.

## Why Use pyproject.toml?

- **Standardization**: One file to rule them all
- **Modern**: Supports modern Python packaging tools
- **Readable**: TOML format is more readable than INI or Python
- **Flexible**: Can configure multiple tools in one place
- **Future-proof**: The future of Python packaging

## Basic Structure

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-package"
version = "0.1.0"
description = "A sample package"
authors = [
    { name = "Your Name", email = "your.email@example.com" }
]
dependencies = [
    "requests>=2.28.0",
    "pandas>=1.5.0"
]

[tool.black]
line-length = 88
target-version = ['py38']

[tool.isort]
profile = "black"
multi_line_output = 3
```

## Common Tool Configurations

- **ruff**: Linting and formatting
- **isort**: Import sorting
- **mypy**: Type checking
- **pytest**: Testing
- **coverage**: Test coverage
