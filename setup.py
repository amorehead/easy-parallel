from setuptools import setup

setup(
    name='easy-parallel-py3',
    py_modules=['parallel-py3'],
    url='https://github.com/amorehead/easy-parallel',
    version='0.1.6.2',
    description='Parallel wrapper for easy multi-threading.',
    long_description=open("README.rst").read(),
    author='Raphael Townshend',
    license='MIT',
    install_requires=['pathos'],
)
