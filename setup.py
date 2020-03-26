import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="infstruments",
    version="0.0.1",
    author="Martin Brösamle",
    author_email="m@martinbroesamle.de",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Instruments for quantifying textual information.",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Filters",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires='>=3.7',
    url="https://github.com/broesamle/infstruments",
    keywords=["natural language processing",
              "string classification",
              "character frequency"],
)
