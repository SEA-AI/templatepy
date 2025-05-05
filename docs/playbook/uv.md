# uv: The Fast Python Package Manager

## What is uv?

An extremely fast Python package and project manager, written in Rust.

![Ruff Performance Comparison](https://github.com/astral-sh/uv/assets/1309177/03aa9163-1c79-4a87-a31d-7a9311ed9310#only-dark){ loading=lazy }

It's developed by [Astral](https://astral.sh/) and is designed to be a drop-in replacement for pip with significant performance improvements. Find the documentation [here](https://docs.astral.sh/uv/).

!!! info "What does uv stand for?"
    Nothing in specific, here's a [comment](https://github.com/astral-sh/uv/issues/1349#issuecomment-1986451785) from the uv repo:

    `uv` was given to us on PyPI, is Astral-themed (i.e. ultraviolet or universal), and is short and easy to type.

## Why is uv Cool?

- **Speed**: Up to 10-100x faster than pip
- **Reliability**: Better dependency resolution
- **Compatibility**: Works with existing requirements.txt and pyproject.toml
- **Modern**: Written in Rust for performance
- **Simple**: Familiar interface for pip users

## Getting Started

### Installation

```bash
# Using curl
curl -LsSf https://astral.sh/uv/install.sh | sh

# Using pip
pip install uv
```

### Basic Commands

```bash
# Install packages
uv pip install pandas numpy

# Install from requirements.txt
uv pip install -r requirements.txt

# Create a virtual environment
uv venv

# Install in editable mode
uv pip install -e .
```

### Key Features

- **Fast Installation**: Parallel downloads and installations
- **Smart Caching**: Efficient package caching
- **Virtual Environments**: Built-in venv support
- **Wheel Building**: Fast wheel building for local packages
- **Lock Files**: Generate and use lock files for reproducible installations

## Documentation

For more information, visit the official documentation:
- [uv Documentation](https://github.com/astral-sh/uv)
- [GitHub Repository](https://github.com/astral-sh/uv)

## Best Practices

- Use lock files for reproducible environments
- Leverage the cache for faster installations
- Use virtual environments for project isolation
- Consider using `uv` in CI/CD pipelines for faster builds 