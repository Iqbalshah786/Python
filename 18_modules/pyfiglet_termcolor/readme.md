# pyfiglet and termcolor modules

This project demonstrates how to use `pyfiglet` and `termcolor` to print colored ASCII art in Python.

## directory Structure


- `myenv/`: The virtual environment directory (not included in the repository).
- `app.py`: The main Python script.


## Prerequisites

- Python 3.x installed on your system.
- `pip` (Python package installer).

## Setup

### macOS and Linux

1. **Create a virtual environment**:

    ```sh
    python3 -m venv myenv
    ```

2. **Activate the virtual environment**:

    ```sh
    source myenv/bin/activate
    ```

3. **Install dependencies**:

    ```sh
    pip install pyfiglet termcolor
    ```

### Windows

1. **Create a virtual environment**:

    ```sh
    python -m venv myenv
    ```

2. **Activate the virtual environment**:

    ```sh
    myenv\Scripts\activate
    ```

3. **Install dependencies**:

    ```sh
    pip install pyfiglet termcolor
    ```

## Running the Project

1. **Activate the virtual environment** (if not already activated):

    On macOS and Linux:

    ```sh
    source myenv/bin/activate
    ```

    On Windows:

    ```sh
    myenv\Scripts\activate
    ```

2. **Run the script**:

    ```sh
    python app.py
    ```

3. **Follow the prompts** to input the text and the desired color for the ASCII art.

## Deactivating the Virtual Environment

When you're done working, you can deactivate the virtual environment with:

```sh
deactivate
