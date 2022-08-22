from setuptools import find_packages, setup

setup(
    name='financial-dashboard',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires=">=3.9",
    install_requires=[],
    test_suite='tests',
)
