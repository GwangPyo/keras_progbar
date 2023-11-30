from setuptools import setup, find_packages

setup(
    name='progbar',
    version='0.1',
    description='Progress bar of keras',
    author='Keras-team',
    requires=[],
    install_requires=['numpy'],
    packages=find_packages(exclude=[])
)
