import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sescraper",
    version="0.1.2",
    author="miki164",
    author_email="miki3867@gmail.com",
    description="Package to get daily information about the stock market",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/miki164/stock-exchange-scraper",
    packages=setuptools.find_packages(),
    classifiers=[
	"Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
	"Environment :: Handhelds/PDA's",   	
	"Intended Audience :: Developers",
	"Intended Audience :: Information Technology",
	"Intended Audience :: Financial and Insurance Industry",
	"Topic :: Office/Business :: Financial",

    ],
    python_requires='>=3.6',
)
