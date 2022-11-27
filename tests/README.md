## Getting Started - Tests
![tests](https://github.com/jt-kl/jt-snippets/actions/workflows/tests.yml/badge.svg)
![coverage](./coverage.svg)

Setup your Python virtual environment with the corresponding dependant libraries and run the tests by using the following BASH commands:

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
pytest -vvv --cov-report=term-missing --cov=jt_snippets
```