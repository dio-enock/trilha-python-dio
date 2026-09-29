from pathlib import Path

from setuptools import find_packages, setup


BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "README.md", "r", encoding="utf-8") as file:
    page_description = file.read()

with open(BASE_DIR / "requirements.txt", encoding="utf-8") as file:
    requirements = [
        line.strip()
        for line in file
        if line.strip() and not line.startswith("#")
    ]


setup(
    name="pacote-processamento-imagem",
    version="0.1.0",
    author="Fork Charles Changes by Enock",
    description="Pacote Python para processamento e análise de imagens usando scikit-image.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SEU_USUARIO/pacote-processamento-imagem",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=requirements,
    python_requires=">=3.9",
)