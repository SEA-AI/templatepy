# Testing with pytest

## What is pytest?

pytest is a powerful, flexible, and easy-to-use testing framework for Python. It's designed to make testing simple and scalable, with features that make it easy to write and maintain tests.

## Why Use pytest?

- **Simple**: Easy to get started
- **Powerful**: Rich ecosystem of plugins
- **Flexible**: Multiple ways to organize tests
- **Informative**: Detailed failure reports
- **Extensible**: Large plugin ecosystem

## Project Structure

!!! note
    Notice that the `tests` directory is outside of the `my_package` directory. 
    This is a best practice since we do not want to pollute the `my_package` directory with test files.
    Also, the folder structure should mirror the source code structure.

```
my_project/
├── my_package/
│   ├── __init__.py
│   ├── main.py
│   ├── users/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── services.py
│   └── orders/
│       ├── __init__.py
│       ├── models.py
│       └── services.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_main.py
│   ├── users/
│   │   ├── __init__.py
│   │   ├── test_models.py
│   │   └── test_services.py
│   └── orders/
│       ├── __init__.py
│       ├── test_models.py
│       └── test_services.py
├── pyproject.toml
└── README.md
```

## Getting Started

### Installation

```bash
pip install pytest
# or
uv pip install pytest
```

### Basic Test Example

```python
# tests/test_main.py
def test_addition():
    assert 1 + 1 == 2

def test_string_operations():
    assert "hello" + " world" == "hello world"
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_main.py

# Run specific test
pytest tests/test_main.py::test_addition

# Run with verbose output
pytest -v

# Run with print statements
pytest -s
```

## Key Features

### Fixtures

```python
# tests/conftest.py
import pytest

@pytest.fixture
def sample_data():
    return {"key": "value"}

# tests/test_main.py
def test_with_fixture(sample_data):
    assert sample_data["key"] == "value"
```

### Parametrize Tests

```python
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert input * 2 == expected
```

### Markers

```python
@pytest.mark.slow
def test_slow_operation():
    # This test will be skipped unless explicitly run
    pass

# Run only slow tests
pytest -m slow
```

## Best Practices

### Test Organization

- Keep tests in a separate `tests` directory
- Mirror your source code structure 
- Use `conftest.py` for shared fixtures

### Test Naming

- Use descriptive test names
- Follow the pattern `test_<function>_<scenario>`
- Make test names readable

### Test Structure

- Arrange-Act-Assert pattern
- One assertion per test
- Keep tests independent

### Fixtures

- Use fixtures for setup and teardown
- Keep fixtures focused and reusable
- Use `conftest.py` for shared fixtures

### Test Coverage

- Aim for high coverage
- Focus on critical paths
- Don't test implementation details

## Common pytest Plugins

- `pytest-cov`: Coverage reporting
- `pytest-xdist`: Parallel test execution
- `pytest-mock`: Mocking support
- `pytest-asyncio`: Async test support
- `pytest-bdd`: Behavior-driven development

## Configuration

Add to your `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "-v --cov=src" 
```