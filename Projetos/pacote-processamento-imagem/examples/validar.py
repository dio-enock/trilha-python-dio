from pathlib import Path

import numpy as np
from skimage.draw import disk

from process.combinar import (
    encontrar_diferenca,
    transferir_histograma,
)
from process.transformar import redimensionar_imagem
from utils.io import ler_imagem, salvar_imagem
from utils.plot import (
    plot_histogram,
    plot_image,
    plot_result,
)


BASE_DIR = Path(__file__).resolve().parent
RESULTADOS_DIR = BASE_DIR / "resultados"


def criar_imagem_teste(correcao=False):
    """
    Cria uma imagem RGB sintética para os testes.
    """
    altura = 300
    largura = 400

    imagem = np.zeros(
        (altura, largura, 3),
        dtype=np.uint8,
    )

    imagem[:, :, 0] = 60
    imagem[:, :, 1] = 120
    imagem[:, :, 2] = 180

    rr, cc = disk(
        (150, 200),
        80,
        shape=imagem.shape[:2],
    )

    imagem[rr, cc] = [220, 80, 80]

    if correcao:
        rr, cc = disk(
            (150, 280),
            40,
            shape=imagem.shape[:2],
        )

        imagem[rr, cc] = [80, 220, 100]

    return imagem


def main():
    RESULTADOS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    print("=" * 60)
    print("VALIDAÇÃO DO PACOTE DE PROCESSAMENTO DE IMAGEM")
    print("=" * 60)

    print("\n[1/6] Criando imagens de teste...")

    imagem1 = criar_imagem_teste()
    imagem2 = criar_imagem_teste(correcao=True)

    caminho_imagem1 = RESULTADOS_DIR / "imagem1.png"
    caminho_imagem2 = RESULTADOS_DIR / "imagem2.png"

    salvar_imagem(
        imagem1,
        caminho_imagem1,
    )

    salvar_imagem(
        imagem2,
        caminho_imagem2,
    )

    print("OK - imagens criadas.")

    print("\n[2/6] Testando carregamento de imagem...")

    imagem_carregada = ler_imagem(
        caminho_imagem1
    )

    print(
        f"OK - imagem carregada: "
        f"{imagem_carregada.shape}"
    )

    print("\n[3/6] Testando redimensionamento...")

    imagem_redimensionada = redimensionar_imagem(
        imagem_carregada,
        0.5,
    )

    caminho_redimensionada = (
        RESULTADOS_DIR / "imagem_redimensionada.png"
    )

    salvar_imagem(
        imagem_redimensionada,
        caminho_redimensionada,
    )

    print(
        "OK - "
        f"{imagem_carregada.shape} -> "
        f"{imagem_redimensionada.shape}"
    )

    print("\n[4/6] Testando comparação estrutural...")

    diferenca = encontrar_diferenca(
        imagem1,
        imagem2,
    )

    caminho_diferenca = (
        RESULTADOS_DIR / "diferenca.png"
    )

    salvar_imagem(
        diferenca,
        caminho_diferenca,
    )

    print(
        "OK - mapa de diferença criado."
    )

    print("\n[5/6] Testando transferência de histograma...")

    imagem_histograma = transferir_histograma(
        imagem1,
        imagem2,
    )

    caminho_histograma = (
        RESULTADOS_DIR / "histograma_transferido.png"
    )

    salvar_imagem(
        imagem_histograma,
        caminho_histograma,
    )

    print(
        "OK - histograma transferido."
    )

    print("\n[6/6] Testando visualizações...")

    plot_image(imagem1)

    plot_result(
        imagem1,
        imagem2,
        diferenca,
    )

    plot_histogram(imagem1)

    print("\n" + "=" * 60)
    print("VALIDAÇÃO CONCLUÍDA COM SUCESSO")
    print("=" * 60)

    print(
        f"\nResultados salvos em:\n"
        f"{RESULTADOS_DIR}"
    )


if __name__ == "__main__":
    main()