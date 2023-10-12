## Testing - Getting Started

![tests](https://github.com/jt-kl/jt-snippets/actions/workflows/hosted.yml/badge.svg)
![coverage](./coverage.svg)

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

### Scripted - Tox

```shell
#!/bin/bash
$ clear; tox # Scripted multi version tests

```

### Manual

#### Unit Testing

```shell
#!/bin/bash
$ clear; pytest # Standard checks respecting configs from [pyproject.tool.pytest.ini_options]

$ clear; pytest -vvv -s --cov-report=term-missing --cov=jt_web_crawler # With Coverage Report - MANUAL
$ clear; pytest -vvv -s --no-cov # Without Coverage Report (DEBUG Mode) - MANUAL

```

#### Code Linting

```shell
#!/bin/bash
$ clear; ruff . # Standard checks respecting configs from [pyproject.tool.ruff]
$ clear; ruff check --select F401, E711 # Specific compliance checks for F401 and E711

```

#### Type Checking

```shell
#!/bin/bash
$ clear; mypy # Standard checks respecting configs from [pyproject.tool.mypy]
$ clear; mypy ./src # Specific compliance checks on "src" directory

```

#### Coverage Badge Generation

```shell
#!/bin/bash
$ coverage-badge -f -o ./tests/coverage.svg # Generate and park coverage badge in tests directory
```
