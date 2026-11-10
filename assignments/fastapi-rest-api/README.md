# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar livros usando FastAPI. Você praticará métodos HTTP, validação de dados com modelos, códigos de status e documentação automática.

## 📝 Tarefas

### 🛠️ Criar a API e consultar livros

#### Descrição
Use o código inicial para criar a aplicação FastAPI e implementar rotas de consulta. Para executar, instale as dependências com `pip install fastapi uvicorn` e inicie o servidor com `uvicorn starter-code:app --reload`.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI chamada `app`.
- Implementar `GET /health`, retornando `{"status": "ok"}`.
- Implementar `GET /books`, retornando a lista de livros armazenada em memória.
- Permitir consultar a documentação interativa em `/docs`.

### 🛠️ Buscar e adicionar livros

#### Descrição
Implemente a consulta de um livro por identificador e a criação de livros a partir de dados enviados no corpo da requisição.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}` e retornar o livro correspondente.
- Responder com status `404` quando o identificador não corresponder a um livro.
- Validar os campos `title` e `author` usando o modelo Pydantic fornecido.
- Implementar `POST /books`, atribuir um identificador ao novo livro e responder com status `201`.

### 🛠️ Atualizar e remover livros

#### Descrição
Complete as operações de gerenciamento para permitir atualizar ou remover um livro existente.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para atualizar o título e o autor do livro.
- Implementar `DELETE /books/{book_id}` para remover o livro da lista.
- Responder com status `404` quando uma atualização ou remoção solicitar um identificador inexistente.
- Retornar uma confirmação clara após uma atualização ou remoção bem-sucedida.