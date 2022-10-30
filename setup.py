from setuptools import setup

setup(
    name="pgen_cli",
    version="0.1.0",
    py_modules=["pgen_cli"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "pgen = pgen_cli:pgen",
        ]
    },
)
