from commandline_config import Config
import setuptools

with open("README.md", "r",  encoding='UTF-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="commandline_config",
    version="2.1.0",
    author="Naibo Wang",
    author_email="naibowang@foxmail.com",
    description="A library for users to write (experiment in research) configurations in Python Dict or JSON format, while can read parameters from the command line",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NaiboWang/CommandlineConfig",
    packages=setuptools.find_packages(),
    install_requires=['prettytable'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


preset_config = {
    "index": 1,  # Index of party
    "dataset": "mnist",
    'lr': 0.01,  # learning rate
    'normalization': True,
    "multi-information": [1, 0.5, 'test', "TEST"]
}
config = Config(preset_config)
print(config)
print(config.dataset, config["index"])
config.index = 15
