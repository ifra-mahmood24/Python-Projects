from setuptools import setup, find_packages

setup(
    name="cw2",
    version="1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "cw2=CW2.CLI:main",
        ],
    },
)