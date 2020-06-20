"""
Calculate version number based on pyproject.toml.
---
During `poetry install`, Poetry installs the project as if it were a package itself.
You can then pull from the package metadata.
It's a little tricky to get `importlib_metadata` to work with Docker builds.
You have to remove `--no-root` from the _Dockerfile_ and move `importlib-metadata`
to prod dependencies, and you still might get errors after that.

See [poetry#1036](https://github.com/python-poetry/poetry/issues/1036) and
[poetry#144](https://github.com/python-poetry/poetry/issues/144) for more info.
"""

from importlib_metadata import version

__version__ = version(__package__)
