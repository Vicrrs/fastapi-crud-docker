# FastAPI CRUD Docker

Este projeto é uma aplicação CRUD (Create, Read, Update, Delete) desenvolvida com FastAPI, utilizando PostgreSQL como banco de dados e Docker para facilitar o deployment e a configuração do ambiente. O gerenciamento de dependências é feito com Poetry.

## Recursos

- **FastAPI**: Framework moderno, rápido (de alto desempenho), para construir APIs com Python 3.7+.
- **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional poderoso e gratuito.
- **Docker**: Plataforma para desenvolver, enviar e rodar aplicações em containers.
- **Poetry**: Ferramenta para o gerenciamento de dependências e empacotamento em Python.

## Requisitos

- Docker
- Docker Compose

## Como Iniciar

1. **Clone o Repositório**

    ```bash
    git clone https://github.com/SeuUsuario/fastapi-crud-docker.git
    cd fastapi-crud-docker
    ```

2. **Configuração do Ambiente**

    Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

    ```
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=postgres
    DATABASE_URL=postgresql://postgres:postgres@fastapi_db:5432/postgres
    ```

3. **Construir e Rodar com Docker Compose**

    Para construir e iniciar os containers do projeto, execute:

    ```bash
    docker-compose up --build
    ```

    Isso irá iniciar a aplicação FastAPI na porta `8000` e o serviço PostgreSQL na porta `5433` do seu host.

## Utilizando a API

Após iniciar a aplicação, você pode acessar a documentação interativa da API gerada pelo FastAPI em `http://localhost:8000/docs`.

### Rotas da API

- `POST /tasks/`: Criar uma nova tarefa.
- `GET /tasks/`: Listar todas as tarefas.
- `GET /tasks/{task_id}`: Obter uma tarefa específica pelo ID.
- `PUT /tasks/{task_id}`: Atualizar uma tarefa pelo ID.
- `DELETE /tasks/{task_id}`: Deletar uma tarefa pelo ID.

### Exemplo de Requisição

Para criar uma nova tarefa, você pode enviar uma requisição POST para `http://localhost:8000/tasks/` com um corpo JSON como o seguinte:

```json
{
  "title": "Estudar FastAPI",
  "description": "Ler a documentação oficial do FastAPI",
  "completed": false
}
```

## Contribuições

Contribuições são sempre bem-vindas! Por favor, crie um pull request para contribuir.

## Licença

Este projeto está sob a licença [MIT](https://choosealicense.com/licenses/mit/).
