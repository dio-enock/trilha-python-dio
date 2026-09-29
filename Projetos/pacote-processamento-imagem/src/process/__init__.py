"""
Operações de processamento de imagens.
"""

from .combinar import encontrar_diferenca, transferir_histograma
from .transformar import redimensionar_imagem

__all__ = [
    "encontrar_diferenca",
    "transferir_histograma",
    "redimensionar_imagem",
]