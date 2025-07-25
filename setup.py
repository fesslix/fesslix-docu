from setuptools import setup, find_packages

setup(
    name="my_bibext",
    version="0.1",
    package_dir={"": "docs"},  # <--- this tells setuptools to look in 'docs/'
    packages=find_packages(where="docs"),
    install_requires=[
        "pybtex",
    ],
    entry_points={
        "pybtex.style.formatting": [
            "mystyle = my_bibext.mystyle:Style",
        ],
    },
)
