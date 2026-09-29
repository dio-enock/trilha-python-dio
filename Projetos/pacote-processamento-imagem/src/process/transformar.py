from skimage.transform import resize


def redimensionar_imagem(image, proporcao):
    """
    Redimensiona uma imagem de acordo com uma proporção.

    Parameters
    ----------
    image : numpy.ndarray
        Imagem original.

    proporcao : float
        Proporção desejada.

        Exemplo:
            0.5 -> reduz para 50%
            0.25 -> reduz para 25%
            1.0 -> mantém o tamanho

    Returns
    -------
    numpy.ndarray
        Imagem redimensionada.
    """
    if image is None:
        raise ValueError("A imagem não pode ser None.")

    if not 0 < proporcao <= 1:
        raise ValueError(
            "Informe uma proporção maior que 0 e menor ou igual a 1."
        )

    height = max(
        1,
        round(image.shape[0] * proporcao),
    )

    width = max(
        1,
        round(image.shape[1] * proporcao),
    )

    imagem_redimensionada = resize(
        image,
        (height, width),
        anti_aliasing=True,
    )

    return imagem_redimensionada