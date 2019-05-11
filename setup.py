import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='gender-determinator',
    description='Determines the gender of german nouns and provides some convenient methods',
    long_description=README,
    long_description_content_type="text/markdown",
    version='0.1',
    license='LGPL',
    author='Daniel Sendzik',
    author_email="daniel@sendzik.eu",
    url="https://github.com/Alpha200/gender-determinator",
    install_requires=[],
    packages=['genderdeterminator'],
    package_data={'genderdeterminator': ['words.csv']}
)

