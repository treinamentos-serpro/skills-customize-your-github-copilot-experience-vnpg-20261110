# 📘 Atividade: Persistência de Dados com SQLite e FastAPI

## 🎯 Objetivo

Adapte uma API FastAPI de gerenciamento de livros para armazenar os dados em SQLite em vez de mantê-los somente em memória. Você praticará criação de tabelas, consultas SQL parametrizadas e persistência entre reinicializações.

## 📝 Tarefas

### 🛠️ Criar o banco e a tabela

#### Descrição
Prepare o banco SQLite usado pela API e crie a tabela de livros durante a inicialização da aplicação.

#### Requisitos
O programa concluído deve:

- Criar ou abrir o arquivo `books.db` usando o módulo `sqlite3` da biblioteca padrão do Python.
- Criar a tabela `books` caso ela ainda não exista, com `id` como chave primária autoincremental e campos obrigatórios `title` e `author`.
- Fechar as conexões SQLite após cada operação.
- Continuar iniciando a API com `uvicorn starter-code:app --reload` após instalar `fastapi` e `uvicorn` com `pip install fastapi uvicorn`.

### 🛠️ Persistir consultas e novos livros

#### Descrição
Substitua o armazenamento em memória nos endpoints de consulta e criação por operações no banco de dados.

#### Requisitos
O programa concluído deve:

- Fazer `GET /books` retornar todos os livros armazenados no SQLite.
- Fazer `GET /books/{book_id}` retornar o livro solicitado ou responder com status `404` se ele não existir.
- Fazer `POST /books` inserir um livro válido e retornar o registro criado com status `201`.
- Usar consultas SQL parametrizadas para inserir e consultar dados.

### 🛠️ Atualizar, remover e verificar persistência

#### Descrição
Complete as operações de escrita e confirme que os registros continuam disponíveis depois que o servidor for reiniciado.

#### Requisitos
O programa concluído deve:

- Fazer `PUT /books/{book_id}` atualizar o título e o autor, ou responder com status `404` se o livro não existir.
- Fazer `DELETE /books/{book_id}` remover o livro, ou responder com status `404` se ele não existir.
- Usar consultas SQL parametrizadas também nas operações de atualização e remoção.
- Permitir criar um livro, reiniciar o servidor e encontrá-lo novamente com `GET /books/{book_id}`.