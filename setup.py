import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="mojiconverter",
    version="0.0.1",
    description="moji converter",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/venkatzgithub/moji-converter",
    author="Venkat Prasad",
    author_email="imvenkatprasad@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'moji', 'hiragana', 'katakana', 'converter', 'japanese'],
    )
