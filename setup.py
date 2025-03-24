from setuptools import find_packages, setup

setup(
    name="qtile-ebenezer",
    version="0.1.28",
    description="This repository provides a collection of widgets and behaviors spanning Desktop to Qtile Tiling Window Manager.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="William Sena",
    author_email="me@willsena.dev",
    url="https://github.com/williampsena/qtile-ebenezer",
    packages=find_packages(),
    include_package_data=True,
    package_data={"ebenezer": ["py.typed"]},
    install_requires=[
        "requests>=2.34.0",
        "qtile>=0.30.0",
        "pillow>=11.1.0",
        "psutil>=6.2.0",
        "ruamel.yaml>=0.17.0",
        "cairocffi>=1.8.0",
        "click>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "ebenezer=ebenezer.commands.app:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
