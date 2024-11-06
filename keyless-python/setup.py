from setuptools import find_packages, setup

setup(
    name="traitkeyless",
    packages=find_packages(include=["traitkeyless"]),
    version="0.1.0",
    description="Trait Keyless Addresses",
    author="Trait",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)
