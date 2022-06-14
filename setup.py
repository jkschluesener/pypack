#!/usr/bin/env python

import setuptools
import os

if __name__ == "__main__":

    current_script_dir = os.path.dirname(os.path.realpath(__file__))
    package_dir = current_script_dir

    with open(os.path.join(current_script_dir, "README.md"), "r") as f:
        long_description = f.read()

    with open(os.path.join(current_script_dir, "requirements.txt"), "r") as f:
        requirements = f.read().splitlines()

    packages = setuptools.find_packages(package_dir, exclude=("tests",))

    setuptools.setup(
        name="pypack",
        version="0.1",
        url="https://github.com/jkschluesener/pypack",
        author="Jan K. Schluesener",
        author_email="code@jkschluesener.xyz",
        description="A quickstart repo to layout a python package",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license="MIT",
        include_package_data=True,
        packages=packages,
        install_requires=requirements,
        python_requires='>=3.7',
    )
