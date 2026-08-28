# Linux Automation Toolkit

**Author:** Abed Gashtasebi

A Python-based command-line toolkit for system inspection and basic Linux/macOS automation.

## Features

- System information
- Process information
- Network interface information
- Filesystem path inspection
- File and directory information
- Logging
- Error handling
- Command-line interface
- Automated tests with pytest
- Python package building and installation

## Requirements

- Python 3.12 or newer
- psutil

## Installation

Clone the repository and create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the project in editable mode:

```bash
python -m pip install -e .
```

## Usage

Show available commands:

```bash
linux-toolkit --help
```

Show the application version:

```bash
linux-toolkit --version
```

### System Information

Display system information:

```bash
linux-toolkit system
```

### Process Information

Display information about running processes:

```bash
linux-toolkit processes
```

### Network Information

Display network interface information:

```bash
linux-toolkit network
```

### File and Directory Information

Inspect a file:

```bash
linux-toolkit file README.md
```

Inspect a directory:

```bash
linux-toolkit file .
```

## Error Handling

The CLI handles invalid file paths and missing arguments gracefully.

For example:

```bash
linux-toolkit file
```

reports that the `file` command requires a path.

A nonexistent path is also handled without exposing an uncontrolled Python traceback:

```bash
linux-toolkit file /this/path/does/not/exist
```

## Logging

The application uses Python's built-in `logging` module.

Example:

```text
2026-08-28 03:16:47,873 - INFO - Linux Automation Toolkit started
```

Logging information is separated from the main program output.

## Testing

The project uses `pytest` for automated testing.

Run the complete test suite with:

```bash
python -m pytest
```

The current test suite contains **21 tests** covering the project's core functionality and CLI behavior.

The project includes both:

- Unit tests
- CLI integration tests

## Packaging

The project uses modern Python packaging through:

```text
pyproject.toml
```

Build the package with:

```bash
python -m build
```

This produces:

- Wheel (`.whl`)
- Source distribution (`.tar.gz`)

The command-line application is exposed through the following entry point:

```text
linux-toolkit
```

The package was also tested by installing the generated Wheel into a clean virtual environment.

## Project Structure

```text
linux-automation-toolkit/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── file_info.py
│   ├── main.py
│   ├── network_info.py
│   ├── process_info.py
│   └── system_monitor.py
│
├── tests/
│   ├── test_cli.py
│   ├── test_file_info.py
│   ├── test_main.py
│   ├── test_network_info.py
│   └── test_process_info.py
│
├── docs/
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt


## Technologies

- Python
- psutil
- argparse
- logging
- pathlib
- pytest
- setuptools
- Git
- GitHub

## Learning Goals

This project was developed as a practical Python project to learn and apply:

- Python modules and functions
- Type hints
- Virtual environments
- Third-party packages
- System information with `psutil`
- Command-line interfaces with `argparse`
- Logging
- Exception handling
- Automated testing with `pytest`
- Unit testing
- CLI integration testing
- Git and GitHub
- Python packaging
- `pyproject.toml`
- Wheel and source distributions
- Editable package installation
- Standard package installation
- Testing packages in a clean environment

###  Project Status

-Version 0.1.0 — Complete

The first version of Linux Automation Toolkit is complete and includes the core functionality, automated tests, command-line interface, error handling, and Python packaging.

Future versions may add additional automation features and extend the test suite.

### Author ###

**Abed Gashtasebi**

Linux Automation Toolkit was developed as a practical project for learning Python development, Linux/macOS system interaction, software testing, Git/GitHub workflows, and Python packaging.
