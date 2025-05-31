# Import Bookmarks from TXT

## Descrição
Este projeto fornece scripts Python para importar facilmente uma lista de URLs de um arquivo de texto (`links.txt`) para o seu navegador da web como favoritos. Ele gera um arquivo HTML que pode ser importado pela maioria dos navegadores modernos.

## Funcionalidades
* Importa links de um arquivo `links.txt` simples.
* Gera um arquivo HTML de favoritos (`import.html`) para fácil importação pelo navegador.
* Tenta abrir automaticamente o arquivo HTML gerado no navegador padrão.
* Opção para importar favoritos para uma pasta especificada no gerenciador de favoritos do navegador (usando `import_bookmarks_with_folder.py`).
* Opção para importar favoritos diretamente sem uma pasta contêiner (usando `import_bookmarks.py`).

## Como Funciona
1.  O script lê uma lista de URLs, uma por linha, de um arquivo `links.txt`. A função `get_links` é responsável por ler o arquivo TXT e retornar uma lista de links.
2.  Em seguida, ele gera um arquivo `import.html`. Este arquivo é estruturado em um formato padrão de favoritos. A função `create_import_html` cria este arquivo.
3.  O script `import_bookmarks_with_folder.py` agrupará esses favoritos em uma pasta chamada "my_bookmarks" (ou um nome personalizado se modificado no script) dentro do arquivo HTML. O script `import_bookmarks.py` os listará diretamente.
4.  Finalmente, o script tenta abrir `import.html` usando o aplicativo padrão do sistema para arquivos HTML (geralmente seu navegador da web). Isso é feito pela função `import_bookmarks` usando `os.system("start import.html")`.
5.  Seu navegador normalmente fornecerá uma opção para importar esses favoritos.

## Requisitos
* Python 3.x
* Um arquivo de texto chamado `links.txt` no mesmo diretório do script, contendo uma URL por linha.

## Uso
1.  **Prepare `links.txt`**: Crie um arquivo chamado `links.txt` no mesmo diretório do script. Adicione uma URL por linha. Por exemplo:
    ```txt
    [https://www.google.com](https://www.google.com)
    [https://www.github.com](https://www.github.com)
    [https://www.python.org](https://www.python.org)
    ```
2.  **Escolha um script**:
    * Para favoritos importados para uma pasta (nome da pasta padrão: "my_bookmarks"): Use `import_bookmarks_with_folder.py`.
    * Para favoritos importados diretamente (sem pasta contêiner): Use `import_bookmarks.py`.
3.  **Execute o script**:
    Abra um terminal ou prompt de comando, navegue até o diretório que contém o script e `links.txt`, e execute o script escolhido:
    ```bash
    python import_bookmarks_with_folder.py
    ```
    ou
    ```bash
    python import_bookmarks.py
    ```
4.  **Importe no Navegador**: Um arquivo `import.html` será criado e deverá abrir automaticamente no seu navegador. Siga as instruções do seu navegador para importar favoritos de um arquivo HTML. Isso geralmente envolve ir ao Gerenciador de Favoritos e encontrar uma opção "Importar Favoritos".

## Descrição dos Arquivos
* `import_bookmarks.py`: Script para importar links para os favoritos do navegador sem uma pasta específica. Ele lê links de `links.txt`, cria `import.html` com os links e tenta abri-lo.
* `import_bookmarks_with_folder.py`: Script para importar links para uma pasta designada (por exemplo, "my_bookmarks") nos favoritos do navegador. Ele lê links de `links.txt`, cria uma pasta no `import.html` se não existir, e adiciona os links a essa pasta, depois tenta abrir o arquivo HTML.
* `links.txt` (criado pelo usuário): Um arquivo de texto simples onde cada linha é uma URL a ser favoritada.
* `import.html` (gerado): O arquivo HTML criado pelos scripts, pronto para importação pelo navegador.

## Personalização (para `import_bookmarks_with_folder.py`)
* Para alterar o nome da pasta padrão de "my_bookmarks", você pode modificar a variável `folder_name` na função `create_import_html` dentro do script `import_bookmarks_with_folder.py`.
    ```python
    def create_import_html(links, folder_name="seu_nome_de_pasta_personalizado_aqui"): #
        # ... o restante da função
    
