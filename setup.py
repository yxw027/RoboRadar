import setuptools
from roboradar import VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="roboradar",
    version=VERSION,
    author="David Johnston",
    author_email="dwjgame11@gmail.com",
    description="Robot position display software for FRC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Short-SirKit-6527/RoboRadar",
    install_requires=[
        "pynetworktables",
        "pint"
    ],
    packages=[
        "roboradar"
        ],
    package_data={
        "roboradar": [
            "icon.png",
            "icon.ico",
            "RoboRadarConfig.json",
            "utils/__init__.py",
            "utils/dummyboxbot.py",
            "fields/__init__.py",
            "fields/FRC_2020.py",
            "robots/__init__.py",
            "robots/standard.py"
            ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
