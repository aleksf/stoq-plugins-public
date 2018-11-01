from setuptools import setup, find_packages

setup(
    name="ole",
    version="2.0.0",
    author="Marcus LaFerrera (@mlaferrera)",
    url="https://github.com/PUNCH-Cyber/stoq-plugins-public",
    license="Apache License 2.0",
    description="Extract objects from OLE payloads",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['olefile>=0.46', 'oletools>=0.53.1'],
    package_data={'ole': ['*.stoq']},
)
