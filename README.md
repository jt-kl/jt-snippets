# jt-snippets

<!-- ![build](https://github.com/jt-kl/jt-snippets/actions/workflows/build.yml/badge.svg) -->

![tests](https://github.com/jt-kl/jt-snippets/actions/workflows/hosted_test.yml/badge.svg)
![tests](https://github.com/jt-kl/jt-snippets/actions/workflows/premise_test.yml/badge.svg)
![build](https://github.com/jt-kl/jt-snippets/actions/workflows/premise_build.yml/badge.svg)
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

1. Python v3.10.12 or greater
2. PIP v22.3.1 or greater

## Getting Started

```shell
#!/bin/bash
$ cd jt-snippets
$ python3 -m venv .env
$ source .env/bin/activate
$ python3 -m pip install --upgrade pip
$ pip3 install wheel --no-cache-dir
$ pip3 install -r requirements-dev.txt --no-cache-dir
$ pip3 install redist/* # If applicable
$ pip3 install -e . # Install 'src' as local library

```

## Testing

```shell
#!/bin/bash
$ clear; tox # Scripted multi version tests

```

## Build & Distribute

Create a redistributable wheel file

```shell
#!/bin/bash
# Build the wheel file and on completion, distribute the wheel file located in
# the "dist" directory. The "build" and "dist" directory can be safely removed

$ python3 scripts/upgrade.py <options> # Updates package version number
$ bash build.sh

```
