from setuptools import setup, find_packages

setup(
    name = "gom-client",
    version = "0.1",
    packages = find_packages(exclude=['tests']),
    scripts = ['gom_client.py']
    )