# Pre-commit Hooks

## What is pre-commit?

pre-commit is a framework for managing and maintaining Git pre-commit hooks. It helps ensure code quality by running checks before each commit, preventing bad commits from entering your repository.

## Why Use pre-commit?

- **Consistency**: Enforce consistent code style across the project
- **Quality**: Catch issues before they enter the repository
- **Automation**: Automate common checks and fixes
- **Team Collaboration**: Share the same checks across the team
- **Time Saving**: Prevent issues early in the development process

## Getting Started

### Installation

```bash
# Using pip
pip install pre-commit

# Using uv
uv pip install pre-commit
```

### Basic Configuration

Create a `.pre-commit-config.yaml` file in your project root:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-ast
      - id: check-json
      - id: check-merge-conflict
      - id: detect-private-key

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
```

### Installation in Repository

```bash
# Install the pre-commit hooks
pre-commit install

# Run against all files
pre-commit run --all-files
```

## Common Hooks

### Code Style
- **ruff**: Fast Python linter
- **black**: Code formatter
- **isort**: Import sorter

### Type Checking
- **mypy**: Static type checker
- **pyright**: Type checker

### Security
- **bandit**: Security linter
- **safety**: Dependency checker
- **detect-secrets**: Secrets detection

### Documentation
- **docformatter**: Docstring formatter
- **pydocstyle**: Docstring style checker

### Testing

!!! warning "Performance Impact"
    Running tests before every commit can be computationally expensive and slow down your workflow. Enable test hooks based on your team's needs and preferences.

- **pytest**: Run tests
- **coverage**: Check test coverage

## Best Practices

### Hook Selection
- Choose hooks that match your project needs
- Start with essential hooks and add more gradually
- Consider performance impact

### Configuration
- Keep configurations in version control
- Document any custom configurations
- Use consistent settings across the team

### Performance
- Use fast hooks for common checks
- Configure hooks to run only on relevant files
- Consider using cached results

### Maintenance
- Keep hooks up to date
- Review and update configurations regularly
- Monitor hook performance

## Troubleshooting

### Hook Failing
- Check hook documentation
- Verify configuration
- Run hook manually for debugging

### Performance Issues
- Use `--verbose` flag to identify slow hooks
- Consider excluding certain files
- Use caching where available

### False Positives
- Configure hooks to ignore specific patterns
- Use inline comments to disable hooks
- Adjust hook settings

## Additional Resources

- [pre-commit Documentation](https://pre-commit.com/)
- [pre-commit-hooks Repository](https://github.com/pre-commit/pre-commit-hooks)
- [Awesome pre-commit hooks](https://github.com/pre-commit/pre-commit-hooks)
