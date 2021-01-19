import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imdbscraper",
    version="0.0.1",
    author="dzalta",
    author_email="dovilezal@gmail.com",
    description="IMDb scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dovilez/IMDbscraper",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas', 'beautifulsoup4'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)