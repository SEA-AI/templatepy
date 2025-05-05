# VS Code Settings

## Recommended Settings

Here are our recommended VS Code settings for Python development. These settings are optimized for our development workflow and integrate well with the tools we use.

### Python Development Settings

```json
{
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        }
    }
}
```

These settings:
- Use Ruff as the default formatter for Python files
- Enable format on save
- Configure import organization to run explicitly

### Testing Configuration

```json
{
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```

This configuration:
- Sets up pytest as the default test runner
- Configures the tests directory
- Disables unittest in favor of pytest

### Code Quality Tools

```json
{
    "sonarlint.connectedMode.project": {
        "connectionId": "sea-ai",
        "projectKey": "SEA-AI_seavision"
    },
    "pylint.ignorePatterns": [
        "*test*.py"
    ]
}
```

These settings:
- Configure SonarLint for code quality analysis
- Set up Pylint to ignore test files

### File Management

```json
{
    "files.exclude": {
        "**/.mypy_cache": true,
        "**/.pytest_cache": true,
        "**/.ruff_cache": true
    }
}
```

This helps keep your workspace clean by hiding:
- Type checking cache files
- Test cache directories
- Linter cache files

### Additional Features

```json
{
    "emojisense.languages": {
        "python": true
    }
}
```

Enables emoji support in Python files.

## Recommended Extensions

1. **Python** (Microsoft)
   - Python language support
   - IntelliSense
   - Linting
   - Debugging

2. **Ruff** (Astral)
   - Fast Python linter
   - Code formatting
   - Import organization

3. **Pylance** (Microsoft)
   - Fast, feature-rich language support
   - Type checking
   - Auto-completion

4. **SonarLint** (SonarSource)
   - Code quality and security
   - Real-time feedback
   - Best practices enforcement

5. **GitLens** (GitKraken)
   - Enhanced Git capabilities
   - Blame annotations
   - History visualization

6. **Markdown All in One** (Yu Zhang)
   - Markdown support
   - Preview
   - Auto-completion

## Best Practices

1. **Workspace Settings**
   - Use workspace settings for project-specific configurations
   - Share settings with team members
   - Document any custom settings

2. **Extension Management**
   - Keep extensions up to date
   - Remove unused extensions
   - Use recommended extensions list

3. **Keyboard Shortcuts**
   - Learn common shortcuts
   - Customize for your workflow
   - Use command palette (Cmd/Ctrl + Shift + P)

4. **Integrated Terminal**
   - Use the integrated terminal
   - Configure your preferred shell
   - Use multiple terminals when needed

## Troubleshooting

Common issues and solutions:

1. **Formatting Not Working**
   - Check if Ruff is installed
   - Verify extension is enabled
   - Check file associations

2. **Linting Issues**
   - Clear cache files
   - Restart VS Code
   - Check extension settings

3. **Performance Problems**
   - Disable unnecessary extensions
   - Clear workspace storage
   - Check file watchers 