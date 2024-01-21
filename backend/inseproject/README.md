# INSE

## Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Configuração do Ambiente

1. Clone o repositório:

    ```bash
    git clone https://github.com/daneccc/inse
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd inseproject
    ```

3. Crie um arquivo `.env` no diretório raiz e configure as variáveis de ambiente:

    ```env
    DEBUG=True
    SECRET_KEY=sua_chave_secreta
    DATABASE_URL=postgres://seu_usuario:senha@postgres:5432/seu_banco_de_dados
    ```

    Substitua `sua_chave_secreta`, `seu_usuario`, `senha` e `seu_banco_de_dados` pelos valores apropriados.

4. Inicialize os serviços usando o Docker Compose:

    ```bash
    docker-compose up -d --build
    ```

5. Acesse a aplicação em [http://localhost:8000](http://localhost:8000)

## Rotas da API

### Detalhes da Escola
- **GET** `/schools/<int:pk>/`: Obtém detalhes da escola por ID.

### Escolas por Estado
- **GET** `/schools/by-state/<int:co_uf>/`: Obtém escolas por estado.

### Escolas por Cidade
- **GET** `/schools/by-city/<int:co_municipio>/`: Obtém escolas por cidade.

### Escolas por Tipo de Rede
- **GET** `/schools/by-network-type/<int:tp_tipo_rede>/`: Obtém escolas por tipo de rede.

### Escolas por Localização
- **GET** `/schools/by-location/<int:tp_localizacao>/`: Obtém escolas por localização.

### Escolas Filtradas
- **GET** `/schools/filtered/`: Obtém escolas com multiplos filtros.

### Escolas Ordenadas por Média INSE Descendente
- **GET** `/schools/ordered/media-inse/descending/`: Obtém escolas ordenadas por média INSE de forma descendente.

### Escolas Ordenadas por Média INSE Ascendente
- **GET** `/schools/ordered/media-inse/ascending/`: Obtém escolas ordenadas por média INSE de forma ascendente.

### Escolas Ordenadas por Número de Estudantes Descendente
- **GET** `/schools/ordered/students/descending/`: Obtém escolas ordenadas por número de estudantes de forma descendente.

### Escolas Ordenadas por Número de Estudantes Ascendente
- **GET** `/schools/ordered/students/ascending/`: Obtém escolas ordenadas por número de estudantes de forma ascendente.

### Documentação da API
- **GET** `/api/schema/docs/`: Documentação interativa da API.
