from setuptools import setup, find_packages
from os import path

# Lê a descrição longa do arquivo README.md
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="ms_toolkit",
    version="0.1.0",
    packages=find_packages(),  # Encontra pacotes automaticamente
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scipy",
    ],
    description="Pacote para manipulação, limpeza e visualização de dados.",
    long_description=long_description,  # Adiciona a descrição longa do README.md
    long_description_content_type="text/markdown",  # Define o tipo de conteúdo como Markdown
    author="Mamadu Sama",
    author_email="mamadusama19@gmail.com",
    url="https://github.com/mamadusama/ms_toolkit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires='>=3.6',  # Define a versão mínima do Python
)
