from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='horizons',
    version='0.1.0',
    description='JPL HORIZONS System client',
    long_description=readme,
    author='David Dupre',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
)
