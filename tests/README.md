## Getting Started - Tests
![tests](https://github.com/jt-kl/jt-snippets/actions/workflows/tests.yml/badge.svg)
![coverage](./tests/coverage.svg)

Setup your Python virtual environment with the corresponding dependant libraries and run the tests by using the following BASH commands:

```sh
#!/bin/bash
# Create a Python virtual environment

$ cd jt_snippets
$ python3 -m venv .env
$ source .env/bin/activate

# Install dependant libraries

$ pip3 install wheel --no-cache-dir
$ pip3 install -r requirements.txt --no-cache-dir

# Run the test suite

$ pytest -vvv
```