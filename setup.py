from setuptools import setup, find_packages
from pathlib import Path
long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name="entropypass",
    version="0.1",
    description="A Python-based tool to generate high-entropy passwords using Leet substitutions and entropy optimization.",
    author="Anantha Krishna Anumanchipalli",
    author_email="anumanchipalli.a@northeastern.edu",
    url="https://github.com/Tcookie47/entropypass",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "entropypass=entropypass.cli:main"
        ],
    },
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
