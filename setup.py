import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="x",
    version="0.0.6",
    author="L",
    author_email="l@x-cmd.com",
    description="X Cmd Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/x-cmd/python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


