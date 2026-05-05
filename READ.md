# Cantinho da Arte

**Cantinho da Arte** é uma aplicação web feita com **Python** e **Streamlit** que funciona como uma galeria digital de obras de arte. O projeto busca imagens diretamente no **Wikimedia Commons**, organiza os resultados por movimentos artísticos e permite navegar por diferentes obras em uma interface visual escura, elegante e inspirada em museus.

Além da visualização das obras, o sistema também possui uma opção de gerar contexto artístico com IA, explicando a obra, o movimento artístico e sua importância cultural.

---

## Demonstração geral

A aplicação permite:

- Visualizar obras de arte em uma galeria interativa.
- Filtrar obras por movimento artístico.
- Buscar obras relacionadas a um artista específico.
- Navegar entre obras com botões de anterior, próxima e aleatória.
- Carregar novos lotes de obras.
- Abrir a imagem em modo ampliado.
- Acessar a página original da obra no Wikimedia Commons.
- Gerar contexto com IA sobre a obra exibida.

---

## Tecnologias utilizadas

O projeto foi desenvolvido usando:

- **Python**
- **Streamlit**
- **Requests**
- **OpenAI API**
- **python-dotenv**
- **Wikimedia Commons API**
- **HTML e CSS customizado dentro do Streamlit**

---

## Estrutura do projeto

```text
Cantinho da arte/
│
├── app.py
├── requirements.txt
├── .gitignore
│
└── src/
    │
    ├── config.py
    ├── state.py
    ├── styles.py
    │
    ├── data/
    │   ├── __init__.py
    │   ├── filters.py
    │   └── movements.py
    │
    ├── services/
    │   ├── __init__.py
    │   ├── ai.py
    │   └── commons.py
    │
    ├── ui/
    │   ├── __init__.py
    │   ├── gallery.py
    │   └── sidebar.py
    │
    └── utils/
        ├── __init__.py
        ├── artwork.py
        └── text.py
```

---

## Descrição dos principais arquivos

### `app.py`

Arquivo principal da aplicação.

Ele configura a página do Streamlit, inicializa o estado da sessão, carrega as obras e renderiza a interface principal.

Responsabilidades:

- Configurar título, layout e sidebar.
- Carregar o primeiro lote de obras.
- Renderizar a barra lateral.
- Renderizar a galeria principal.
- Exibir avisos caso nenhuma obra seja encontrada.

---

### `src/config.py`

Arquivo de configurações globais do projeto.

Contém:

- Título da aplicação.
- Layout da página.
- Estado inicial da sidebar.
- URL da API do Wikimedia Commons.
- Cabeçalhos das requisições.
- Movimento artístico padrão.
- Largura padrão das imagens.
- Limites de busca.
- Chave da API da OpenAI via variável de ambiente.

---

### `src/state.py`

Gerencia o estado da aplicação usando `st.session_state`.

Controla informações como:

- Lista atual de obras carregadas.
- Índice da obra atual.
- Movimento artístico selecionado.
- Nome do artista pesquisado.
- Resolução das imagens.
- Contexto gerado por IA.
- Recarregamento de lotes.

---

### `src/styles.py`

Contém o CSS global da aplicação.

Esse arquivo define o visual da galeria, incluindo:

- Tema escuro.
- Fontes personalizadas.
- Estilo dos botões.
- Estilo da sidebar.
- Área de visualização da imagem.
- Modo de zoom.
- Caixa de contexto gerado por IA.
- Cores e espaçamentos da interface.

---

### `src/data/movements.py`

Contém os movimentos artísticos disponíveis na aplicação.

Cada movimento artístico é associado a uma query de busca usada na API do Wikimedia Commons.

Exemplos de movimentos:

- Arte Grega
- Arte Romana
- Arte Bizantina
- Românico
- Gótico
- Renascimento
- Barroco
- Rococó
- Neoclassicismo
- Romantismo
- Realismo
- Impressionismo
- Pós-Impressionismo
- Expressionismo
- Cubismo
- Futurismo
- Dadaísmo
- Surrealismo

---

### `src/data/filters.py`

Contém listas de filtros usados para melhorar a qualidade dos resultados.

Esses filtros ajudam a remover arquivos que provavelmente não são obras de arte, como:

- PDFs
- Páginas de catálogo
- Capas de livro
- Arquivos `.djvu`
- Arquivos `.svg`
- Páginas digitalizadas
- Materiais de anúncio

Também define termos que ajudam a identificar obras de arte, como:

- `painting`
- `canvas`
- `portrait`
- `fresco`
- `drawing`
- `engraving`
- `óleo`
- `tela`
- `retrato`
- `gravura`

---

### `src/services/commons.py`

Responsável pela comunicação com a API do Wikimedia Commons.

Esse arquivo faz:

- Busca de imagens.
- Leitura dos metadados das obras.
- Conversão dos dados da API para um formato usado pela aplicação.
- Cache das buscas com `st.cache_data`.
- Remoção de duplicatas.
- Aplicação de filtros de qualidade.
- Ordenação dos resultados.
- Busca por movimento artístico.
- Busca por nome de artista.

---

### `src/services/ai.py`

Responsável por gerar contexto artístico usando a API da OpenAI.

A função principal recebe:

- Nome da obra.
- Movimento artístico.
- Chave da API.

E retorna um texto explicativo em português sobre:

- Contexto histórico.
- Características visuais.
- Técnicas utilizadas.
- Importância cultural.

Caso a chave da API não esteja configurada ou ocorra algum erro, a aplicação exibe uma mensagem informando que não foi possível gerar o contexto.

---

### `src/ui/sidebar.py`

Renderiza a barra lateral da aplicação.

A sidebar permite:

- Escolher o movimento artístico.
- Buscar por artista.
- Ajustar a resolução da imagem.
- Carregar um novo lote de obras.
- Sortear obras aleatórias.
- Gerar contexto com IA.

---

### `src/ui/gallery.py`

Renderiza a área principal da galeria.

Esse arquivo cuida de:

- Cabeçalho da aplicação.
- Botões de navegação.
- Contador de obras.
- Exibição da imagem.
- Zoom ao clicar na obra.
- Título da obra.
- Badge do movimento artístico.
- Links para a página no Commons e imagem original.
- Exibição do contexto gerado por IA.

---

### `src/utils/artwork.py`

Contém funções auxiliares para análise e pontuação das obras.

Esse arquivo verifica:

- Se a extensão do arquivo é válida.
- Se o resultado parece uma obra de arte.
- Se o arquivo parece ser documento, catálogo ou página digitalizada.
- Se o nome do artista aparece nos metadados.
- Uma pontuação para ordenar os melhores resultados.

---

### `src/utils/text.py`

Contém funções auxiliares para tratamento de texto.

Inclui funções para:

- Normalizar texto.
- Remover HTML.
- Compactar espaços.
- Extrair valores dos metadados retornados pelo Wikimedia Commons.

---

## Como instalar e rodar o projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
cd "Cantinho da arte"
```

Ou, caso o projeto já esteja na sua máquina, apenas abra a pasta no VS Code.

---

### 2. Criar um ambiente virtual

No Windows:

```bash
python -m venv venv
```

Ativar o ambiente:

```bash
venv\Scripts\activate
```

No Linux ou macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

Caso o `requirements.txt` apresente algum erro de leitura, recrie o arquivo com este conteúdo:

```text
streamlit
requests
openai
python-dotenv
```

Depois rode novamente:

```bash
pip install -r requirements.txt
```

---

### 4. Configurar a chave da OpenAI

A chave da OpenAI é opcional.

Sem ela, a galeria continua funcionando normalmente, mas o botão de contexto com IA não conseguirá gerar explicações.

Para configurar, crie um arquivo chamado `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_aqui
```

Exemplo da estrutura:

```text
Cantinho da arte/
│
├── app.py
├── requirements.txt
├── .env
└── src/
```

---

### 5. Rodar a aplicação

Com o ambiente virtual ativado, execute:

```bash
streamlit run app.py
```

Depois disso, o Streamlit abrirá a aplicação no navegador.

Normalmente o endereço local será algo como:

```text
http://localhost:8501
```

---

## Como usar a aplicação

Ao abrir o projeto no navegador, a aplicação carregará automaticamente um lote inicial de obras.

Na barra lateral, é possível:

1. Escolher um movimento artístico.
2. Digitar o nome de um artista.
3. Ajustar a resolução da imagem.
4. Carregar novas obras.
5. Sortear uma obra aleatória.
6. Gerar contexto com IA.

Na área principal, é possível:

- Ver a imagem da obra.
- Clicar na imagem para ampliar.
- Navegar entre obras.
- Abrir a página original no Wikimedia Commons.
- Abrir a imagem original.
- Ler o contexto gerado pela IA, caso a função esteja configurada.

---

## Movimentos artísticos disponíveis

A aplicação possui vários movimentos artísticos cadastrados, entre eles:

- Grega
- Romana
- Paleocristã
- Bizantina
- Românica
- Gótica
- Renascimento
- Maneirismo
- Barroco
- Rococó
- Neoclassicismo
- Romantismo
- Realismo
- Impressionismo
- Pós-Impressionismo
- Expressionismo
- Cubismo
- Futurismo
- Dadaísmo
- Surrealismo

Cada movimento usa palavras-chave específicas para buscar obras relacionadas no Wikimedia Commons.

---

## Funcionamento da busca

A busca funciona usando a API pública do Wikimedia Commons.

O processo geral é:

1. O usuário escolhe um movimento artístico.
2. O sistema monta uma query de busca.
3. A API do Wikimedia Commons retorna arquivos relacionados.
4. O sistema filtra arquivos inválidos.
5. O sistema remove documentos, catálogos e arquivos não desejados.
6. As obras são pontuadas.
7. As melhores imagens são exibidas na galeria.

Quando o usuário informa um artista, o sistema tenta encontrar correspondências no título, metadados, descrição e categorias das imagens.

---

## Sistema de pontuação das obras

O projeto possui uma lógica simples de pontuação para priorizar resultados melhores.

A pontuação leva em conta:

- Se o arquivo tem extensão válida.
- Se o item parece ser uma obra de arte.
- Se o nome do artista aparece nos metadados.
- Se o nome do artista aparece no título.
- Se o nome do artista aparece na descrição.
- Se a imagem contém termos relacionados a arte.
- Se o arquivo parece ser catálogo, livro ou documento.

Resultados com pontuação maior aparecem primeiro.

---

## Funcionalidade de IA

A aplicação possui uma função opcional de contexto com IA.

Quando o botão **“Contexto com IA”** é usado, o sistema envia para a API:

- O título da obra.
- O movimento artístico selecionado.

A IA retorna uma explicação curta em português sobre a obra.

Essa função depende da variável de ambiente:

```env
OPENAI_API_KEY
```

Caso essa variável não esteja configurada, a aplicação mostra uma mensagem informando que não foi possível gerar o contexto.

---

## Personalização visual

O visual da aplicação está concentrado no arquivo:

```text
src/styles.py
```

Nele é possível alterar:

- Cor de fundo.
- Cores dos textos.
- Bordas.
- Fonte dos títulos.
- Fonte dos textos.
- Estilo dos botões.
- Tamanho da imagem.
- Estilo da sidebar.
- Caixa de contexto da IA.
- Comportamento visual do zoom.

---

## Possíveis melhorias futuras

Algumas ideias para evoluir o projeto:

- Adicionar favoritos.
- Salvar obras curtidas pelo usuário.
- Criar página de detalhes para cada obra.
- Adicionar filtros por período histórico.
- Adicionar filtros por país.
- Adicionar filtros por técnica artística.
- Melhorar a busca por artista.
- Criar histórico de obras visualizadas.
- Adicionar modo apresentação.
- Adicionar download de imagem.
- Adicionar tradução automática de metadados.
- Criar deploy público da aplicação.
- Adicionar testes automatizados.
- Melhorar tratamento de erros da API.
- Adicionar paginação real dos resultados.

---

## Problemas comuns

### O comando `streamlit` não é reconhecido

Instale o Streamlit:

```bash
pip install streamlit
```

Depois rode novamente:

```bash
streamlit run app.py
```

---

### A aplicação não encontra obras

Isso pode acontecer quando:

- A API do Wikimedia Commons demora para responder.
- O filtro de artista é específico demais.
- O movimento selecionado retorna poucos resultados.
- A internet está instável.

Tente:

- Clicar em **Carregar**.
- Clicar em **Aleatório**.
- Remover o nome do artista.
- Escolher outro movimento artístico.

---

### O contexto com IA não funciona

Verifique se o arquivo `.env` existe e contém:

```env
OPENAI_API_KEY=sua_chave_aqui
```

Também confira se a dependência `python-dotenv` está instalada:

```bash
pip install python-dotenv
```

---

### As imagens demoram para carregar

A aplicação busca imagens externas no Wikimedia Commons.

Se estiver lento, tente diminuir a resolução na sidebar.

```

---

## Créditos

As imagens e metadados das obras são obtidos por meio do **Wikimedia Commons**, uma base pública de arquivos de mídia.

O projeto utiliza a API do Wikimedia Commons para buscar e exibir obras de arte dentro da aplicação.

---

## Licença

Este projeto é de uso educacional e pode ser adaptado livremente.

Ao utilizar imagens exibidas pela aplicação, consulte sempre a página original da obra no Wikimedia Commons para verificar a licença específica de cada arquivo.

---

## Autor

Projeto desenvolvido por **Vinícius Andrade**.
