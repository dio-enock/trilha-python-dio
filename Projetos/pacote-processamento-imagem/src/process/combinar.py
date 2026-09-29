import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def _converter_para_gray(image):
    """
    Converte uma imagem para escala de cinza quando necessário.
    """
    if image.ndim == 2:
        return image

    if image.ndim == 3:
        return rgb2gray(image)

    raise ValueError(
        "A imagem deve possuir 2 dimensões (grayscale) "
        "ou 3 dimensões (RGB/RGBA)."
    )


def encontrar_diferenca(image1, image2):
    """
    Compara duas imagens utilizando Structural Similarity (SSIM).

    Parameters
    ----------
    image1 : numpy.ndarray
        Primeira imagem.
    image2 : numpy.ndarray
        Segunda imagem.

    Returns
    -------
    numpy.ndarray
        Mapa normalizado das diferenças estruturais.
    """
    if image1 is None or image2 is None:
        raise ValueError("As duas imagens são obrigatórias.")

    if image1.shape != image2.shape:
        raise ValueError(
            "Informe 2 imagens com o mesmo formato."
        )

    gray_image1 = _converter_para_gray(image1)
    gray_image2 = _converter_para_gray(image2)

    score, diff_image = structural_similarity(
        gray_image1,
        gray_image2,
        full=True,
        data_range=float(
            max(
                gray_image1.max(),
                gray_image2.max(),
            )
            - min(
                gray_image1.min(),
                gray_image2.min(),
            )
        ),
    )

    print(f"Similaridade das imagens: {score:.4f}")

    min_value = diff_image.min()
    max_value = diff_image.max()

    if max_value == min_value:
        return np.zeros_like(diff_image)

    diff_image_normalizado = (
        diff_image - min_value
    ) / (max_value - min_value)

    return diff_image_normalizado


def transferir_histograma(image1, image2):
    """
    Transfere a distribuição de cores/histograma de image2 para image1.

    Parameters
    ----------
    image1 : numpy.ndarray
        Imagem cuja distribuição será modificada.

    image2 : numpy.ndarray
        Imagem utilizada como referência.

    Returns
    -------
    numpy.ndarray
        Imagem com o histograma ajustado.
    """
    if image1 is None or image2 is None:
        raise ValueError(
            "As duas imagens são obrigatórias."
        )

    if image1.ndim != image2.ndim:
        raise ValueError(
            "As imagens devem possuir o mesmo número de dimensões."
        )

    if image1.ndim == 2:
        return match_histograms(
            image1,
            image2,
        )

    if image1.ndim == 3:
        if image1.shape[2] != image2.shape[2]:
            raise ValueError(
                "As imagens devem possuir a mesma quantidade de canais."
            )

        return match_histograms(
            image1,
            image2,
            channel_axis=-1,
        )

    raise ValueError(
        "As imagens devem ser grayscale ou possuir canais de cor."
    )