# FileBridge

## Setup Instructions

To initialize the project and set up the Python environment:

1. Open a command prompt in the project root directory.
2. Run the setup script:
	```
	.\setup.bat
	```
3. The script will:
	- Check if a virtual environment named `venv` exists.
	- If not present, create the environment and install dependencies from `requirements.txt`.
	- If present, activate the environment.

After setup, you can activate the environment manually with:
```
venv\Scripts\activate.bat
```

## Working with the Application

To start the FileBridge application and open the frontend:

1. Make sure your virtual environment is activated (see above).
2. Start the Streamlit application by running:
	```
	streamlit run app.py
	```
3. After starting, open your web browser and go to the URL displayed in the terminal (usually http://localhost:8501).

Refer to project documentation for additional details or configuration options.


## Quality Assurance Measures

This section describes the steps and tools used to ensure code quality and reliability. Additional measures will be added as the project evolves.

### Code Reformatting

To ensure consistent code style, use [black](https://black.readthedocs.io/) to automatically format all Python files. Run the following command in PowerShell from the project root:

```
black .
```

### Linting

To check for code quality issues and enforce coding standards, use [pylint](https://pylint.pycqa.org/). Run the following command in PowerShell from the project root:

```
pylint app.py src tests --fail-under=10.0
```

### Type Checking

To check for type correctness and catch type-related errors, use [mypy](https://mypy.readthedocs.io/). Run the following command in PowerShell from the project root:

```
mypy app.py src
```

### Test Execution and Code Coverage

To run all available tests and check code coverage, use [pytest](https://docs.pytest.org/en/stable/) together with [pytest-cov](https://pytest-cov.readthedocs.io/). Run the following command in PowerShell from the project root:

```
pytest --cov=src --cov-report=term-missing --cov-fail-under=100
```

### Code Complexity

To keep track of code complexity and maintainability, use [radon](https://radon.readthedocs.io/). Run the following command in PowerShell from the project root:

```
radon mi app.py src tests
```

## Changelog
[Style Guide](https://github.com/vweevers/common-changelog/tree/main)

### 0.1.0 - 2025-08-17

_First release._

#### Added

- Basic web page layout added with all application tabs ("Synchronization", "Configuration", "Documentation")
- Added view for file system and file system stats to "Synchronization" page
- Added FileSystem handler to collect folder and file data from the system