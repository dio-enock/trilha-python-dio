"""
Utilitários para leitura, gravação e visualização de imagens.
"""

from .io import ler_imagem, salvar_imagem
from .plot import plot_histogram, plot_image, plot_result

__all__ = [
    "ler_imagem",
    "salvar_imagem",
    "plot_image",
    "plot_result",
    "plot_histogram",
]