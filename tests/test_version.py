from portfolio import __version__


def test_version():
    """Verify version number in __init__.py."""
    assert __version__ == "0.3.0"
