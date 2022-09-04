# jt-snippets
Code snippets

# Requirements

1. Python v3.10.4 or greater


# Test

To run the test suite, execute the following BASH commands

```sh
#!/bin/bash
# Create a Python virtual environment

$ cd jt_snippets
$ python3 -m venv .env
$ source .env/bin/activate

# Install library dependencies

$ pip3 install wheel --no-cache-dir
$ pip3 install -r requirements.txt --no-cache-dir
$ pip3 install -e .

# Run the tests

$ pytest -vvv
```