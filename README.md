# jt-snippets

<!-- ![build](https://github.com/jt-kl/jt-snippets/actions/workflows/build.yml/badge.svg) -->
![tests](https://github.com/jt-kl/jt-snippets/actions/workflows/tests.yml/badge.svg)
![coverage](./tests/coverage.svg)

The following project contains helper functions/methods to complement your Python code

## Breakdown

1. Callback operations
2. CSV operations
3. Data generator operations
4. Data type operations
5. Date/Time type operations
6. Decorator operations
7. IO operations
8. Logger operations
9. Validation operators

## Requirements

Requirements to use the library:

1. Python v3.10.6
2. PIP v22.2.2

## Build & Distribute

Create a redistributable wheel file

```shell
#!/bin/bash
# Create a Python virtual environment

$ cd jt-snippets
$ python3 -m venv .env
$ source .env/bin/activate

# Install library dependencies

$ pip3 install wheel --no-cache-dir
$ pip3 install -r requirements.txt --no-cache-dir

# Build the wheel file and on completion, distribute the wheel file 
# located in the "dist" directory. The "build" and/or "dist" 
# directory can be safely removed

$ python3 -m build
```

## Testing

```shell
#!/bin/bash
# Create a Python virtual environment

$ cd jt-snippets
$ python3 -m venv .env
$ source .env/bin/activate

# Install library dependencies

$ pip3 install wheel --no-cache-dir
$ pip3 install -r requirements.txt --no-cache-dir
$ pip3 install -e .

# Execute tests
pytest
```
