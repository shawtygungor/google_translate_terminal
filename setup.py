from setuptools import find_packages, setup

setup(
    name="terminal_translate",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={"console_scripts": ["translate=src.main:main"]},
)
