# Algorithm Problems and Solutions

This repository contains solutions to various algorithm problems with detailed documentation and tests.

## Project Structure

``` bash
algorithms-python/
├── docs/              # Documentation for each problem
│   └── problem-name.md
├── src/              # Source code organized by categories
│   ├── dynamic/      # Dynamic programming problems
│   ├── graphs/       # Graph-related problems
│   ├── math/         # Mathematical problems
│   ├── searching/    # Searching algorithms
│   ├── sorting/      # Sorting algorithms
│   └── strings/      # String manipulation problems
└── tests/            # Test cases for each solution
```

## Documentation Format

Each problem includes:

1. A markdown file in the `docs/` directory explaining:
   - Problem description
   - Algorithm design
   - Input/Output specifications
   - Constraints
   - Solution approach
   - Time and space complexity

2. Implementation in the appropriate category directory under `src/`
3. Test cases in the `tests/` directory

## Getting Started

1. Install dependencies.

   ```bash
   pip install -r requirements.txt
   ```

2. Run tests.

   ```bash
   pytest tests/
   ```

## Contributing

When adding a new problem solution:

1. Create documentation in `docs/`
2. Implement solution in appropriate category in `src/`
3. Add comprehensive tests in `tests/`
4. Ensure all tests pass before submitting
