import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wcapi",
    version="0.1",
    author="Edward Amor",
    author_email="edward.amor3@gmail.com",
    description="Python WebConnect Emulator API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Skellet0r/wcapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.7",
    install_requires=["comtypes"],
)
