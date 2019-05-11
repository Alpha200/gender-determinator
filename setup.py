from setuptools import setup

setup(
    name='gender-determinator',
    description='Determines the gender of german nouns and provides some convenient methods',
    version='0.1',
    license='LGPL',
    author='Daniel Sendzik',
    author_email="daniel@sendzik.eu",
    url="https://github.com/Alpha200/gender-determinator",
    install_requires=[],
    packages=['genderdeterminator'],
    package_data={'genderdeterminator': ['words.csv']}
)
