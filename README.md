# jt-snippets

<!-- ![build](https://github.com/jt-kl/jt-snippets/actions/workflows/build.yml/badge.svg) -->

![tests](https://github.com/jt-kl/jt-snippets/actions/workflows/hosted.yml/badge.svg)
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

1. Python v3.10.6 or greater
2. PIP v22.3.1 or greater

## Development

Clone the repository and setup your environment for development

_Linux (Ubuntu/Debian)_

```shell
#!/bin/bash
# Create a Python virtual environment

$ cd snippets
$ python3 -m venv .env
$ source .env/bin/activate

# Install library dependencies

$ pip3 install wheel --no-cache-dir
$ pip3 install -r requirements.txt --no-cache-dir
$ pip3 install redist/*
$ pip3 install -e .
```

## Linting & Testing

```shell
#!/bin/bash
# Create a Python virtual environment

$ cd jt-snippets
$ python3 -m venv .env
$ source .env/bin/activate

# Install library dependencies

$ pip3 install wheel --no-cache-dir
$ pip3 install -r requirements.txt --no-cache-dir
$ pip3 install redist/*
$ pip3 install -e .

# Execute linting

$ clear; flake8 --count --statistics  --exclude=.env --ignore=F821,F541,E501 --max-complexity=10

# Execute testing

$ clear; pytest -vvv --cov-report=term-missing --cov=jt-snippets

# Execute multiple version testing

$ clear; tox

# Type checking

$ clear; mypy ./src
```

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
$ pip3 install redist/*
$ pip3 install -e .

# Build the wheel file and on completion, distribute the wheel file located in
# the "dist" directory. The "build" and "dist" directory can be safely removed

$ python3 upgrade.py <options>
$ bash build.sh

# Manually execute tests locally and generate a coverage badge and
# check it into the repository
$ clear; coverage-badge -o ./tests/coverage.svg
```
