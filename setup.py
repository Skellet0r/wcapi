import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wccom",
    version="0.0.1",
    author="Edward Amor",
    author_email="edward.amor3@gmail.com",
    description="WCCOM object wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Skellet0r/WCCOM",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
    install_requires=[
        'comtypes'
    ]
)