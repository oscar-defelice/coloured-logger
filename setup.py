""" Setup file for the package."""
#!/usr/bin/env python3
import os
from coloured_logger import (
    __version__,
    __description__,
    __author__,
    __email__,
    __license__,
    __title__,
)
from setuptools import setup, find_packages

pypi_name = "coloured-logger"
pkg_name = "coloured_logger"


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# Read requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

s = setup(
    name=pypi_name,
    version=__version__,
    license=__license__,
    description=__description__,
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    keywords="security,scanner",
    url="https://github.com/oscar-defelice/%s" % pypi_name,
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">= 3.9",
    author=__author__,
    author_email=__email__,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
)
