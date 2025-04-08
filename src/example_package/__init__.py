"""Example package for Cloudsmith assessment."""

try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version  # For Python < 3.8

__version__ = version("example_package")
