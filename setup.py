from setuptools import setup

setup(
    name="pgen",
    version="0.1.0",
    py_modules=["pgen"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "pgen = pgen:pgen",
        ]
    },
)
