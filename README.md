# CodeMapper

CodeMapper is a tool designed to map code repositories for Large Language Model (LLM) editing. It traverses your codebase, extracts key information, and creates a JSON representation that can be easily consumed by LLMs for various code analysis and modification tasks.

## Features

- Traverse entire code repositories
- Extract information from Python files, including:
  - Docstrings
  - Function definitions and signatures
  - Class definitions and methods
  - Import statements
- Handle non-Python files by providing basic file information
- Respect `.gitignore` patterns to exclude irrelevant files
- Automatically exclude `.git` directories and `.DS_Store` files
- Generate a comprehensive JSON map of the repository

    Note:  You can exclude more directories by adding them to .gitignore or adding them to the 
    traverser.py file.

## Installation

You can install CodeMapper directly from GitHub using pip:

```sh
pip install git+https://github.com/MikeyBeez/codemapper.git
```

## Usage

To use CodeMapper, run the following command in your terminal:

```sh
codemapper /path/to/repo /path/to/.gitignore output.json
```

- `/path/to/repo`: The root directory of the repository you want to map
- `/path/to/.gitignore`: The path to the .gitignore file to use for excluding files
- `output.json`: The name of the output file where the JSON map will be saved

### Example

```sh
codemapper /Users/username/Projects/my-project /Users/username/Projects/my-project/.gitignore my-project-map.json
```

This command will analyze the `my-project` repository, respect the rules in its `.gitignore` file, and save the resulting map to `my-project-map.json`.

### Output

The tool generates a JSON file containing:

- File paths and types
- For Python files:
  - Docstrings
  - Function definitions and signatures
  - Class definitions and methods
  - Import statements
- For non-Python files:
  - Basic file information (path, type, size)

Note: `.git` directories and `.DS_Store` files are automatically excluded from the output.

## Project Structure

- `src/codemapper/`: Main package directory
  - `cli.py`: Command-line interface implementation
  - `parser.py`: Code for parsing Python files and extracting information
  - `traverser.py`: Repository traversal logic
  - `utils.py`: Utility functions for creating the code map
- `tests/`: Directory containing test files
- `setup.py`: Package and distribution management
- `LICENSE`: MIT License file

## Contributing

Contributions to CodeMapper are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

Please make sure to update tests as appropriate and adhere to the project's coding standards.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, please open an issue on the GitHub repository.

Thank you for using or contributing to CodeMapper!
