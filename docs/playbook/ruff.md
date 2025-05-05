# Ruff

## What is Ruff?

An extremely fast Python linter and code formatter, written in Rust.

![Ruff Performance Comparison](https://user-images.githubusercontent.com/1309177/232603514-c95e9b0f-6b31-43de-9a80-9e844173fd6a.svg#only-dark){ loading=lazy }


The [Ruff Linter](https://docs.astral.sh/ruff/linter/) is an extremely fast Python linter designed as a drop-in replacement for Flake8 (plus dozens of plugins), isort, pydocstyle, pyupgrade, autoflake, and more.

The [Ruff formatter](https://docs.astral.sh/ruff/formatter/) is an extremely fast Python code formatter designed as a drop-in replacement for `Black`, available as part of the ruff CLI via `ruff format`.

!!! info "What does uv stand for?"
    Not sure, but my guess would be "RUst Fast Formatter". Some other creative names are 

## Why is Ruff Cool?

- **Speed**: Up to 10-100x faster than traditional linters
- **Comprehensive**: Implements 500+ [rules](https://docs.astral.sh/ruff/rules/) from popular linters
- **Modern**: Written in Rust for performance
- **Configurable**: Highly customizable rule sets
- **Compatible**: Works with existing tool configurations

## Getting Started

### Installation

```bash
# Using pip
pip install ruff

# Using uv
uv pip install ruff
```

### Basic Usage

```bash
# Lint your code
ruff check .

# Fix automatically fixable issues
ruff check --fix .

# Show available rules
ruff rule list
```

### Configuration

Add to your `pyproject.toml`:

```toml
[tool.ruff]
# Enable all rules
select = ["E", "F", "B", "I"]

# Ignore specific rules
ignore = ["E501"]

# Line length
line-length = 88

# Target Python version
target-version = "py38"
```

## Key Features

- **Fast**: Parallel processing of files
- **Comprehensive**: Implements rules from:
  - flake8
  - isort
  - pyupgrade
  - autoflake
  - and many more
- **Configurable**: Fine-grained control over rules
- **IDE Integration**: Works with VS Code, PyCharm, etc.

## Documentation

For more information, visit:
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [GitHub Repository](https://github.com/astral-sh/ruff)

## Best Practices

- Start with a basic rule set and gradually add more
- Use auto-fix where possible
- Configure rules to match your team's style guide
- Integrate with your IDE for real-time feedback
- Use in CI/CD pipelines for consistent code quality 