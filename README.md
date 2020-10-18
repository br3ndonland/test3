# Getting Started Testing: pytest edition

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/en/stable/)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![hooks](https://github.com/br3ndonland/test3/workflows/hooks/badge.svg)](https://github.com/br3ndonland/test3/actions)
[![tests](https://github.com/br3ndonland/test3/workflows/tests/badge.svg)](https://github.com/br3ndonland/test3/actions)

Brendon Smith ([br3ndonland](https://github.com/br3ndonland/))

## Description

This repository contains material from the Boston Python User Group's meetup on February 26, 2020, "[Getting Started Testing: pytest edition](https://www.meetup.com/bostonpython/events/266720542/)," led by Ned Batchelder. The slides and code from Ned Batchelder are available [here](https://nedbatchelder.com/text/test3.html).

Meetup description:

> Presentation night sponsored by Kyruus, hosted by PTC.
>
> Ned Batchelder, Getting Started Testing
>
> Do you want to learn how to write automated tests in Python with pytest? We'll start from the very beginning! See how pytest works, and how to write tests. Once the basics are covered, we'll get into fixtures, parameterization, and coverage measurement. Then we'll do a few more advanced topics: including test doubles (mocks and fakes).
>
> It's a lot to cover, but we'll take our time and work through it. You'll get everything you need to start writing your own tests.
>
> The talk is available now if you want a preview: https://bit.ly/pytest3
>
> Doors open at 5:30 for mingling, networking, and exploring the PTC tech space. The presentation starts at 6:30.

This repository was generated from my [template-python repository](https://github.com/br3ndonland/template-python). For more info on template repositories, see [GitHub's announcement](https://github.blog/2019-06-06-generate-new-repositories-with-repository-templates/).

## Quickstart

```sh
❯ cd path/to/repo
# Install virtual environment with poetry: https://python-poetry.org/docs/
❯ poetry install
❯ poetry shell
# Install pre-commit hooks
.venv ❯ pre-commit install
# Try running the tests
.venv ❯ pytest
.venv ❯ coverage run -m pytest tests
```

## Presentation notes

### Part 1

#### First principles

- Writing tests is an upfront time commitment that actually saves time in the long-run.
- Testing is the "flossing of software." It feels like a chore, and everyone feels like they should be doing more. "Writing tests is serious effort that takes real time."
- Test frameworks all seem weird at first. The way you write for test frameworks is much different than the ways you write your actual code. There are new conventions to learn.

#### Test frameworks

- `unittest` is wordy and not Pythonic, because it was lifted from the Java jUnit framework.
- Nose is not maintained and should no longer be used. It was called nose because it would "sniff" out your tests automatically, rather than having you specify where they are.
- Pytest uses functions instead of classes. Ned admits that pytest is very powerful, and does many things that even he doesn't understand.
- Project structure (slide 21)

  - Put your tests in the _tests/_ directory.
  - When I moved the tests to the _tests/_ directory, pytest started throwing a `ModuleNotFoundError`. Pytest could find the tests in the _tests/_ directory, but the tests couldn't find the modules they were importing from the root directory. The solution, as explained on [Stack Overflow](https://stackoverflow.com/questions/10253826), is to simply create an empty _conftest.py_ file in the root directory. The _conftest.py_ file is typically used for storing pytest fixtures, as explained below.
  - When referencing Python modules in different directories, use the syntax `directory.module`. For example:

    ```py
    # tests/test_port6_pytest.py

    import pytest

    from portfolio.portfolio2 import Portfolio
    ```

- Running tests (slide 22)
  - Set up, act, assert.
  - See [test_port1_pytest.py](tests/test_port1_pytest.py) for a good example.
  - Try it: `pytest -q tests/test_port1_pytest.py`
  - To skip tests that are intentionally broken for the sake of example (in the modules ending in _broken.py_), either tell pytest to skip them at run time with `pytest -k "not broken"`, or [mark the tests as expected to fail and skip them](https://docs.pytest.org/en/latest/skipping.html) with `import pytest` and then by adding `@pytest.mark.xfail()` as a [decorator](https://docs.python.org/3/whatsnew/2.4.html#pep-318-decorators-for-functions-and-methods) above the applicable test function.
  - `unittest` provides a similar `@unittest.expectedFailure` decorator.
- Test isolation (slide 27):
  - Tests shouldn't affect each other.
  - If one test fails, it shouldn't stop the subsequent tests.

#### Fixtures

- Slide 32
- [pytest fixtures](https://docs.pytest.org/en/latest/fixture.html) use [decorators](https://docs.python.org/3/whatsnew/2.4.html#pep-318-decorators-for-functions-and-methods) to create reusable test methods.
- In [test_port6_pytest.py](tests/test_port6_pytest.py), we use a fixture to initialize class `Portfolio()` with some test data.
- The _conftest.py_ file is normally used for [sharing fixture functions](https://docs.pytest.org/en/latest/fixture.html#conftest-py-sharing-fixture-functions).

### Part 2

#### Coverage

- Coverage is like a test of your tests. It evaluates how much of your production code is actually being run by your tests.
- It's not always necessary to get to 100% coverage.
- Even if you are at 100%, it doesn't mean your application works perfectly.

#### Test doubles

- Test doubles stand in for real application data. Useful for simulating application dependencies.
- In this example, we use some pre-set stock prices as test doubles, instead of calling the stock pricing API. We also replace the Requests API call with a `FakeRequests` method.
- Mocks are more powerful test doubles. The [pytest-mock](https://github.com/pytest-dev/pytest-mock/) `mocker.patch` fixture can replace (patch) application data with a mock object.

#### Testability

- You may sometimes need to refactor code in order to make it more testable.
- In particular, it may be helpful to separate code into smaller units.

#### Summing up

- Testing is complicated, important, worthy, and rewarding.
- The drawings were by Ned's son Ben, including "sleepy snake," the mascot for [coverage.py](https://github.com/nedbat/coveragepy).

## Further information

See [CONTRIBUTING.md](.github/CONTRIBUTING.md).
