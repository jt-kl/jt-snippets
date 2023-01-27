## Getting Started - Tests
![tests](https://github.com/jt-kl/jt-snippets/actions/workflows/hosted.yml/badge.svg)
![coverage](./coverage.svg)

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
$ clear; flake8 --count --show-source --statistics  --exclude=.env --ignore=F821,F541,E501 --max-complexity=10

# Execute testing

pytest -vvv --cov-report=term-missing --cov=jt-snippets
```
