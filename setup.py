from typing import List

from setuptools import setup

import finders


def read_requirements(filepath) -> List[str]:
    with open(filepath, "r") as f:
        return f.read().splitlines(keepends=False)


setup(
    name='project_stop_finder',
    version=finders.__version__,
    packages=['finders'],
    url='https://github.com/sylvaus/project_stop_finder',
    author='sylvaus',
    description='Tutorial Project',
    extra_requires={"test": read_requirements("test_requirements.txt")}
)
