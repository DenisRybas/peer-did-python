import pathlib

from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="peerdid",
    version="0.1.0",
    description="PeerDID for Python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sicpa-dlab/peer-did-python",
    author="",
    author_email="",
    license="Apache-2.0",
    python_requires=">=3.5",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
    packages=["peerdid"],
    install_requires=[],
    test_requires=['pytest']
)
