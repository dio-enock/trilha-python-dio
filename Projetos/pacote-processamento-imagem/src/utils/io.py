from pathlib import Path

import numpy as np
from skimage.io import imread, imsave
from skimage.util import img_as_ubyte


def ler_imagem(path, is_gray=False):
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(
            f"Imagem não encontrada: {path}"
        )

    return imread(
        path,
        as_gray=is_gray,
    )


def _preparar_imagem_para_salvar(image):
    """
    Converte a imagem para um formato compatível
    com arquivos de imagem comuns.
    """
    if not isinstance(image, np.ndarray):
        image = np.asarray(image)

    if image.size == 0:
        raise ValueError(
            "Não é possível salvar uma imagem vazia."
        )

    if np.issubdtype(image.dtype, np.floating):
        image = np.clip(
            image,
            0.0,
            1.0,
        )
        image = img_as_ubyte(image)

    elif image.dtype != np.uint8:
        image = np.clip(
            image,
            0,
            255,
        ).astype(np.uint8)

    return image


def salvar_imagem(image, path):
    if image is None:
        raise ValueError(
            "A imagem não pode ser None."
        )

    path = Path(path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    imagem_pronta = _preparar_imagem_para_salvar(
        image
    )

    imsave(
        path,
        imagem_pronta,
    )


def salvar_image(image, path):
    salvar_imagem(
        image,
        path,
    )