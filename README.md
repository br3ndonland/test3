# Getting Started Testing: pytest edition

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
![pre-commit](https://github.com/br3ndonland/test3/workflows/pre-commit/badge.svg)
![test](https://github.com/br3ndonland/test3/workflows/test/badge.svg)

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
portfolio-hash-py3.7 ❯ pre-commit install
# Try running the tests
portfolio-hash-py3.7 ❯ pytest
portfolio-hash-py3.7 ❯ coverage run -m pytest tests
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
  - When I moved the tests to the _tests/_ directory, pytest started throwing a `ModuleNotFoundError`. Pytest could find the tests in the _tests/_ directory, but the tests couldn't find the modules they were importing from the root directory. The solution, as explained on [Stack Overflow](https://stackoverflow.com/questions/10253826), is to simply create an empty _conftest.py_ file in the root directory. This seems strange to me.
  - An alternative recommended in the [pytest docs under "Good Integration practices"](https://docs.pytest.org/en/latest/goodpractices.html) is to create a _setup.py_ file and then run `pip install -e .`. This project doesn't need a separate `setup.py` because it's managed automatically by Poetry.
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
- Fixtures use [decorators](https://docs.python.org/3/whatsnew/2.4.html#pep-318-decorators-for-functions-and-methods) to create reusable test methods.
- In [test_port6_pytest.py](tests/test_port6_pytest.py), we use a fixture to initialize class `Portfolio()` with some test data.
- See [pytest docs on fixtures](https://docs.pytest.org/en/latest/fixture.html).
- The _conftest.py_ file is normally used for [sharing fixture functions](https://docs.pytest.org/en/latest/fixture.html#conftest-py-sharing-fixture-functions).

## Repository contents

- [.github/](.github): configuration files for [GitHub](https://github.com/).
  - [ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE)
    - [bug_report.md](.github/ISSUE_TEMPLATE/bug_report.md): template for filing a bug report issue on GitHub.
    - [feature_request.md](.github/ISSUE_TEMPLATE/feature_request.md): template for filing a feature request issue on GitHub.
  - [workflows/](.github/workflows)
    - [pre-commit.yml](.github/workflows/pre-commit.yml): [GitHub Actions](https://github.com/features/actions) workflow that runs the pre-commit hooks specified in [.pre-commit-config.yaml](.pre-commit-config.yaml).
    - [test.yml](.github/workflows/test.yml): [GitHub Actions](https://github.com/features/actions) workflow that runs Python tests.
  - [CODE_OF_CONDUCT.md](.github/CODE_OF_CONDUCT.md): guidelines for behavior when contributing to open-source projects.
  - [CONTRIBUTING.md](.github/CONTRIBUTING.md): detailed instructions for using this repository.
  - [PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md): template for submitting [GitHub pull requests](.github/CONTRIBUTING.md).
- [.vscode/settings.json](.vscode/settings.json): default settings for [VSCode](https://code.visualstudio.com/).
- [.pre-commit-config.yaml](.pre-commit-config.yaml): configuration file for [pre-commit](https://pre-commit.com/) specifying [Git pre-commit hooks](https://www.git-scm.com/docs/githooks).
- [LICENSE](LICENSE): [license](https://choosealicense.com/) file describing how the repository may be legally used.
- [poetry.lock](poetry.lock): lock file used by [Poetry](https://python-poetry.org/) to install specific versions of each dependency.
- [pyproject.toml](pyproject.toml): configuration file for [Poetry](https://python-poetry.org/).
- [README.md](README.md): this file, a concise description of the repository

## Further information

See [CONTRIBUTING.md](.github/CONTRIBUTING.md).
