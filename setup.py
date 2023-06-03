#!/usr/bin/python3
import sys
import setuptools
from setuptools.command.install import install

version = sys.version_info[:2]
if (3, 0) < version < (3, 4):
    print('greet_me requires Python version 3.4 or later ({}.{} detected).'.format(*version))
    sys.exit(1)

setuptools.setup(
    name='greet_me',
    version='0.1',
    description='Greet Me App',
    author='Veerendra Kakumanu',
    packages=setuptools.find_packages(where="src"),
    install_requires=["waitress", "Flask"],
    entry_points={'console_scripts': [
        'greet_me = greet_me:main']},
    package_dir={'': 'src'},
    python_requires=">=3.4",
    classifiers=[
        "Programming Language :: Python :: 3.4",
        "Development Status :: 4 - Beta"
    ],
    zip_safe=False)