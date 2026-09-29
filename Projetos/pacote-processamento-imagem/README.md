# Pacote Processamento de Imagem

Pacote Python desenvolvido para realizar operações básicas de processamento e análise de imagens utilizando principalmente as bibliotecas [scikit-image](https://scikit-image.org/), [NumPy](https://numpy.org/) e [Matplotlib](https://matplotlib.org/).

O projeto disponibiliza funcionalidades para:

* comparação de histogramas;
* transferência de histogramas;
* análise de similaridade estrutural;
* geração de mapas de diferença;
* redimensionamento de imagens;
* carregamento de imagens;
* salvamento de imagens;
* exibição de imagens;
* exibição de resultados;
* exibição de histogramas.

---

## Tecnologias

* Python 3.9+
* NumPy
* scikit-image
* Matplotlib
* setuptools

---

## Estrutura do projeto

```text
pacote-processamento-imagem/
├── README.md
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── process/
│   │   ├── __init__.py
│   │   ├── combinar.py
│   │   └── transformar.py
│   └── utils/
│       ├── __init__.py
│       ├── io.py
│       └── plot.py
└── examples/
    └── validar.py
```

---

# Instalação

## 1. Clonar ou acessar o projeto

Entre no diretório do projeto:

```bash
cd Projetos/pacote-processamento-imagem
```

---

## 2. Criar o ambiente virtual

Linux/macOS:

```bash
python3 -m venv .venv
```

Windows:

```powershell
python -m venv .venv
```

---

## 3. Ativar o ambiente virtual

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
.venv\Scripts\activate
```

Depois da ativação, o terminal deverá apresentar algo semelhante a:

```text
(.venv) usuario@computador:~/Projetos/pacote-processamento-imagem$
```

---

## 4. Atualizar o pip

```bash
python -m pip install --upgrade pip
```

---

## 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

# Instalação do próprio pacote

Com o ambiente virtual ativado, execute:

```bash
pip install -e .
```

O parâmetro `-e` instala o projeto em modo editável.

Isso é útil durante o desenvolvimento porque alterações no código do pacote ficam disponíveis sem a necessidade de reinstalar o projeto a cada modificação.

---

# Validando a instalação

Antes de executar o exemplo, verifique se as bibliotecas estão disponíveis:

```bash
python -c "import numpy; import skimage; import matplotlib; print('Dependências OK')"
```

A saída esperada é:

```text
Dependências OK
```

Também é possível verificar o pacote:

```bash
python -c "from process import redimensionar_imagem; print('Pacote OK')"
```

Saída esperada:

```text
Pacote OK
```

---

# Validação das funcionalidades

O projeto possui um exemplo completo em:

```text
examples/validar.py
```

Ele cria imagens sintéticas e executa as principais funcionalidades do pacote.

Execute:

```bash
python examples/validar.py
```

O programa executará:

1. criação de imagens de teste;
2. carregamento de imagem;
3. redimensionamento;
4. comparação estrutural;
5. transferência de histograma;
6. exibição de imagens;
7. exibição do resultado da comparação;
8. exibição dos histogramas.

---

# Resultados

Durante a execução será criada a pasta:

```text
examples/resultados/
```

Contendo arquivos semelhantes a:

```text
resultados/
├── imagem1.png
├── imagem2.png
├── imagem_redimensionada.png
├── diferenca.png
└── histograma_transferido.png
```

Além dos arquivos gerados, o Matplotlib abrirá as janelas para visualização das imagens e histogramas.

---

# Funcionalidades

## Carregar imagem

Utilize:

```python
from utils.io import ler_imagem

imagem = ler_imagem("imagem.png")
```

Para carregar diretamente em escala de cinza:

```python
imagem = ler_imagem(
    "imagem.png",
    is_gray=True,
)
```

---

## Salvar imagem

```python
from utils.io import salvar_imagem

salvar_imagem(
    imagem,
    "resultado.png",
)
```

O diretório de destino será criado automaticamente quando necessário.

---

## Redimensionar imagem

```python
from process.transformar import redimensionar_imagem

imagem_redimensionada = redimensionar_imagem(
    imagem,
    0.5,
)
```

A proporção determina o tamanho final.

examples:

```text
1.0  -> 100%
0.75 -> 75%
0.5  -> 50%
0.25 -> 25%
```

Exemplo:

```python
imagem_redimensionada = redimensionar_imagem(
    imagem,
    0.5,
)
```

Uma imagem de:

```text
1200 x 800
```

será transformada aproximadamente em:

```text
600 x 400
```

---

# Similaridade estrutural

O projeto utiliza o **Structural Similarity Index Measure (SSIM)** para comparar duas imagens.

```python
from process.combinar import encontrar_diferenca

diferenca = encontrar_diferenca(
    imagem1,
    imagem2,
)
```

O método:

1. verifica se as imagens possuem o mesmo formato;
2. converte as imagens para escala de cinza;
3. calcula o índice SSIM;
4. imprime a similaridade;
5. gera um mapa normalizado das diferenças.

Exemplo de saída:

```text
Similaridade das imagens: 0.9342
```

Quanto mais próximo de `1`, maior a similaridade estrutural entre as imagens.

O retorno é uma imagem que pode ser visualizada:

```python
from utils.plot import plot_image

plot_image(diferenca)
```

---

# Transferência de histograma

A transferência de histograma utiliza uma segunda imagem como referência para modificar a distribuição de intensidades da primeira.

```python
from process.combinar import transferir_histograma

resultado = transferir_histograma(
    imagem1,
    imagem2,
)
```

A imagem `imagem1` é modificada para possuir uma distribuição de intensidade semelhante à de `imagem2`.

Para visualizar:

```python
from utils.plot import plot_result

plot_result(
    imagem1,
    imagem2,
    resultado,
)
```

---

# Exibir imagem

```python
from utils.plot import plot_image

plot_image(imagem)
```

O método detecta automaticamente imagens grayscale e imagens coloridas.

---

# Exibir resultados

É possível visualizar várias imagens lado a lado:

```python
from utils.plot import plot_result

plot_result(
    imagem_original,
    imagem_referencia,
    resultado,
)
```

A última imagem será identificada como:

```text
Result
```

---

# Exibir histograma

Para imagens RGB:

```python
from utils.plot import plot_histogram

plot_histogram(imagem)
```

Serão apresentados os histogramas dos canais:

```text
Red
Green
Blue
```

Para imagens em escala de cinza, será exibido um único histograma.

---

# Exemplo completo

```python
from process.combinar import (
    encontrar_diferenca,
    transferir_histograma,
)
from process.transformar import redimensionar_imagem
from utils.io import (
    ler_imagem,
    salvar_imagem,
)
from utils.plot import (
    plot_histogram,
    plot_image,
    plot_result,
)


imagem1 = ler_imagem("imagem1.png")
imagem2 = ler_imagem("imagem2.png")


# Redimensionamento
imagem_redimensionada = redimensionar_imagem(
    imagem1,
    0.5,
)

salvar_imagem(
    imagem_redimensionada,
    "imagem_redimensionada.png",
)


# Similaridade estrutural
diferenca = encontrar_diferenca(
    imagem1,
    imagem2,
)

salvar_imagem(
    diferenca,
    "diferenca.png",
)


# Transferência de histograma
resultado_histograma = transferir_histograma(
    imagem1,
    imagem2,
)

salvar_imagem(
    resultado_histograma,
    "histograma_transferido.png",
)


# Visualização
plot_image(imagem1)

plot_result(
    imagem1,
    imagem2,
    diferenca,
)

plot_histogram(imagem1)
```

---

# Fluxo recomendado para desenvolvimento

Depois de criar o ambiente:

```bash
python3 -m venv .venv
```

Ative:

```bash
source .venv/bin/activate
```

Instale:

```bash
pip install -r requirements.txt
pip install -e .
```

Valide:

```bash
python examples/validar.py
```

Após alterar o código, execute novamente:

```bash
python examples/validar.py
```

Como o pacote está instalado em modo editável, não é necessário executar novamente:

```bash
pip install -e .
```

a cada alteração.

---

# Desativando o ambiente virtual

Quando terminar:

```bash
deactivate
```

---

# Resumo das funcionalidades

| Funcionalidade              | Implementação             |
| --------------------------- | ------------------------- |
| Carregar imagem             | `ler_imagem()`            |
| Salvar imagem               | `salvar_imagem()`         |
| Exibir imagem               | `plot_image()`            |
| Exibir resultados           | `plot_result()`           |
| Exibir histograma           | `plot_histogram()`        |
| Similaridade estrutural     | `encontrar_diferenca()`   |
| Mapa de diferenças          | `encontrar_diferenca()`   |
| Transferência de histograma | `transferir_histograma()` |
| Redimensionamento           | `redimensionar_imagem()`  |
| Validação integrada         | `examples/validar.py`     |

---

# Licença

Projeto desenvolvido para fins de estudo e prática de processamento digital de imagens utilizando Python e scikit-image.
