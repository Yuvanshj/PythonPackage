from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Banner",
    version="1.0.0",
    author="Yuvansh Juneja",
    author_email="vujj892@gmail.com",
    description="A Python package for printing a banner",
    long_description=long_description,
    long_description_content_type="text/markdown",

    install_requires=[
        
    ],
    extras_require={
        
    },
    entry_points={
        
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)