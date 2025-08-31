from setuptools import setup, find_packages

setup(
    name="MyPythonApp",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.31",
        "numpy>=1.26"
    ],
    entry_points={
        "console_scripts": [
            "myapp=src.mymodule:main",
        ],
    },
)
