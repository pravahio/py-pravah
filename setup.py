import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pravah",
    version="0.0.1",
    author="Abhishek Upperwal",
    author_email="mesh@soket.in",
    description="Data access layer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pravahio",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'mesh_rpc',
        'pravah_protocols',
        'dlake'
    ]
)