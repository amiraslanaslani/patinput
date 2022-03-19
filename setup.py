from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="patinput",
    version="0.1.0",
    author="Amir Aslan Aslani",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["py-getch==1.0.1"],
    url="https://github.com/amiraslanaslani/patinput",
    project_urls={
        "Bug Tracker": "https://github.com/amiraslanaslani/patinput/issues",
    },
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.6",
)

