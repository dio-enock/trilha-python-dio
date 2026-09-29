import matplotlib.pyplot as plt
import numpy as np


def _configurar_imagem(ax, image):
    """
    Configura a exibição da imagem de acordo com o número de canais.
    """
    if image.ndim == 2:
        ax.imshow(image, cmap="gray")
    else:
        ax.imshow(image)

    ax.axis("off")


def plot_image(image):
    """
    Exibe uma única imagem.
    """
    if image is None:
        raise ValueError("A imagem não pode ser None.")

    plt.figure(figsize=(8, 5))

    ax = plt.gca()
    _configurar_imagem(ax, image)

    plt.tight_layout()
    plt.show()


def plot_result(*args):
    """
    Exibe duas ou mais imagens lado a lado.

    A última imagem é identificada como Result.
    """
    if not args:
        raise ValueError("Informe pelo menos uma imagem.")

    numero_imagens = len(args)

    fig, axes = plt.subplots(
        nrows=1,
        ncols=numero_imagens,
        figsize=(5 * numero_imagens, 4),
    )

    if numero_imagens == 1:
        axes = [axes]
    else:
        axes = np.asarray(axes).flatten()

    names = [
        f"Image{i}"
        for i in range(1, numero_imagens)
    ]

    names.append("Result")

    for ax, name, image in zip(axes, names, args):
        ax.set_title(name)
        _configurar_imagem(ax, image)

    fig.tight_layout()
    plt.show()


def plot_histogram(image):
    """
    Exibe o histograma da imagem.

    Para imagens RGB/RGBA, exibe os histogramas dos canais
    vermelho, verde e azul.

    Para imagens em escala de cinza, exibe um único histograma.
    """
    if image is None:
        raise ValueError("A imagem não pode ser None.")

    if image.ndim == 2:
        fig, ax = plt.subplots(figsize=(8, 4))

        ax.hist(
            image.ravel(),
            bins=256,
            color="gray",
            alpha=0.8,
        )

        ax.set_title("Histograma")
        ax.set_xlabel("Intensidade")
        ax.set_ylabel("Frequência")

        fig.tight_layout()
        plt.show()

        return

    if image.ndim != 3 or image.shape[2] < 3:
        raise ValueError(
            "A imagem deve ser grayscale ou possuir pelo menos "
            "3 canais."
        )

    colors = ["red", "green", "blue"]
    names = ["Vermelho", "Verde", "Azul"]

    fig, axes = plt.subplots(
        nrows=1,
        ncols=3,
        figsize=(12, 4),
    )

    for index, (ax, color, name) in enumerate(
        zip(axes, colors, names)
    ):
        ax.hist(
            image[:, :, index].ravel(),
            bins=256,
            color=color,
            alpha=0.8,
        )

        ax.set_title(f"Histograma {name}")
        ax.set_xlabel("Intensidade")
        ax.set_ylabel("Frequência")

    fig.tight_layout()
    plt.show()