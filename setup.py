#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")


requirements = [
    "nbconvert>=1.3.5",
    "nbformat>=3.0.9",
    "RelevanceAI[notebook]",
    "pyyaml",
    "typing_extensions",
    "python-frontmatter",
]

notebook_test_requirements = [
    "vectorhub[sentence-transformers]>=1.8.3",
    "matplotlib>=3.5.1",
]

dev_requirements = [
    "ipykernel",
    "jupyterlab",
    "autopep8",
    "pylint",
    "flake8",
    "pre-commit",
]

setuptools.setup(
    name="rdme-sync",
    version="0.0.1",
    description="RelevanceAI ReadMe Sync",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="dev@relevance.ai",
    install_requires=requirements,
    extras_require={
        "tests": notebook_test_requirements,
        "dev": dev_requirements + notebook_test_requirements,
    },
    # package_dir={"": "rdme_sync"},
    # packages=setuptools.find_packages(where="rdme_sync"),
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
