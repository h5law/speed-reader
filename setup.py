import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="speed-reader",
    version="1.0.1",
    author="h5law",
    author_email="h5law@pm.me",
    description="A speed reader implemented in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/h5law/speed-reader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    install_requires=["numpy", "click"],
    entry_points={
        'console_scripts': [
            'speed-reader = reader:main',
        ],
    },
)
