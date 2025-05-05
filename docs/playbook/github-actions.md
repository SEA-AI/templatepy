# GitHub Actions

## What are GitHub Actions?

GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. It's integrated directly into GitHub and allows you to create custom workflows for your projects.

## Why Use GitHub Actions?

- **Integrated**: Native GitHub integration
- **Flexible**: Customizable workflows
- **Powerful**: Extensive marketplace of actions
- **Free**: Generous free tier for public repositories
- **Secure**: Built-in secrets management

## Where are Actions Executed?

GitHub Actions run on GitHub-hosted runners or self-hosted runners:

- **GitHub-hosted runners**:
  - Ubuntu Linux
  - Windows
  - macOS
  - Different hardware specifications available

- **Self-hosted runners**:
  - Run on your own infrastructure
  - Custom hardware
  - Custom operating systems
  - Private network access

## When are Actions Executed?

Actions can be triggered by various events:

- **Push events**: When code is pushed to a branch
- **Pull request events**: When a PR is created, updated, or merged
- **Schedule**: Using cron syntax
- **Manual**: Using workflow_dispatch
- **Repository events**: Issues, releases, etc.
- **External events**: Using repository_dispatch

## Basic Workflow Example

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest
```

## Common Use Cases

### 1. Python Testing

```yaml
name: Python Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10']

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest
```

### 2. Code Quality

```yaml
name: Code Quality

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        pip install ruff black
    - name: Run linters
      run: |
        ruff check .
        black --check .
```

### 3. Documentation Deployment

```yaml
name: Deploy Docs

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        pip install mkdocs-material
    - name: Deploy to GitHub Pages
      run: |
        mkdocs gh-deploy --force
```

## Best Practices

1. **Workflow Organization**
   - Keep workflows focused and modular
   - Use reusable workflows
   - Separate concerns (test, lint, deploy)

2. **Security**
   - Use secrets for sensitive data
   - Limit permissions
   - Use dependency caching
   - Pin action versions

3. **Performance**
   - Use caching
   - Run jobs in parallel
   - Use matrix builds
   - Optimize workflow steps

4. **Maintenance**
   - Document workflows
   - Use consistent naming
   - Keep workflows up to date
   - Monitor workflow runs

## Useful Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
- [GitHub Actions Examples](https://github.com/actions/starter-workflows) 