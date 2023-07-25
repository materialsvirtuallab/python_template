"""Package configuration."""

from __future__ import annotations

import platform
import sys

import numpy as np
from setuptools import Extension, find_namespace_packages, setup


with open("README.md") as file:
    long_description = file.read()

setup(
    name="pymatgen",
    packages=find_namespace_packages(
        include=["pymatgen.*", "pymatgen.analysis.*", "pymatgen.io.*", "pymatgen.ext.*", "cmd_line"],
        exclude=["pymatgen.*.tests", "pymatgen.*.*.tests", "pymatgen.*.*.*.tests"],
    ),
    version="2023.7.17",
    python_requires=">=3.8",
    install_requires=[],
    extras_require={},
    # All package data has to be explicitly defined. Do not use automated codes like last time. It adds
    # all sorts of useless files like test files and is prone to path errors.
    package_data={},
    author="Author list",
    author_email="ongsp@ucsd.edu",
    maintainer="Shyue Ping Ong",
    maintainer_email="ongsp@ucsd.edu",
    url="https://materialsvirtuallab.org",
    description="Template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
