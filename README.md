# Algorithm Problems and Solutions

This repository contains solutions to various algorithm problems with detailed documentation and tests.

## Project Structure

```
algorithms-python/
├── docs/              # Documentation for each problem
│   └── problem-name.md
├── src/               # Source code organized by categories
│   ├── dynamic/       # Dynamic programming problems
│   ├── graphs/        # Graph-related problems
│   ├── math/          # Mathematical problems
│   ├── searching/     # Searching algorithms
│   ├── sorting/       # Sorting algorithms
│   └── strings/       # String manipulation problems
└── tests/             # Test cases for each solution
```

## Documentation Format

Each problem includes:

1. A markdown file in the `docs/` directory explaining:

   * Problem description
   * Algorithm design
   * Input/Output specifications
   * Constraints
   * Solution approach
   * Time and space complexity

2. Implementation in the appropriate category directory under `src/`

3. Test cases in the `tests/` directory

## Getting Started

1. Create a virtual environment:

   ```bash
   uv venv
   source .venv/bin/activate
   ```

2. Install dependencies listed in `pyproject.toml`:

   ```bash
   uv sync
   ```

3. Run tests:

   ```bash
   pytest tests/
   ```

4. Format and lint code:

   ```bash
   black src/ tests/
   isort src/ tests/
   ```

## Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality before each commit. Pre-commit automatically runs checks like formatting, linting, and type checking when you attempt to make a commit.

1. Install pre-commit hooks (after installing dependencies):

   ```bash
   pre-commit install
   ```

2. The hooks will run automatically on each commit, but you can also run them manually:

   ```bash
   pre-commit run --all-files
   ```

3. The following checks are configured:
   - Trailing whitespace removal
   - End-of-file fixing
   - YAML validation
   - Large file checking
   - Black (code formatting)
   - isort (import sorting)
   - pylint (linting)
   - mypy (type checking)

## Contributing

When adding a new problem solution:

1. Create documentation in `docs/`
2. Implement solution in appropriate category in `src/`
3. Add comprehensive tests in `tests/`
4. Ensure all tests pass before submitting
