from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="ruaroa-ai",
    version="0.1.4",
    author="Ruaroa AI",
    author_email="contact@ruaroa.ai",
    description="Ruaroa AI - Autonomous AI for Data Science and Machine Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RuaroaAI/ruaroa-ai",
    packages=find_packages(),
    package_data={
        "ruaroa": [
            "../requirements.txt",
            "utils/config.yaml",
            "utils/viz_templates/*",
            "example_tasks/bitcoin_price/*",
            "example_tasks/house_prices/*",
            "example_tasks/*",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ruaroa = ruaroa.run:run",
        ],
    },
)
