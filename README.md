# 📌 Correção de Simulado - FastAPI

Este projeto é uma API desenvolvida em **FastAPI** para processar arquivos CSV contendo respostas de alunos e comparar com o gabarito do simulado. A API gera estatísticas de acertos por aluno e média geral.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.9+**
- **FastAPI** - Framework para construção da API
- **Pandas** - Manipulação e análise de dados
- **Uvicorn** - Servidor ASGI para execução da API

---

## 📂 Estrutura do Projeto

```
.
├── service/
│   ├── processamento.py  # Função para processar os CSVs
│
├── models.py             # Modelos Pydantic
├── utils.py              # Funções auxiliares
├── main.py               # Arquivo principal da API
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação do projeto
```

---

## 🛠️ Instalação e Execução

### 1️⃣ Clonar o Repositório

```sh
 git clone https://github.com/seu-usuario/nome-do-repositorio.git
 cd nome-do-repositorio
```

### 2️⃣ Criar e Ativar um Ambiente Virtual (Recomendado)

```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar Dependências

```sh
pip install -r requirements.txt
```

### 4️⃣ Executar a API

```sh
uvicorn main:app --reload
```

A API será iniciada em: **http://127.0.0.1:8000**

---

## 📌 Endpoints

### 📤 1. Upload dos Arquivos CSV

**Rota:** `/upload-files/`
**Método:** `POST`
**Parâmetros:** Arquivos `gabarito.csv` e `respostas.csv`

#### Exemplo de Requisição `cURL`

```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/upload-files/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'gabarito=@gabarito.csv' \
  -F 'respostas=@respostas.csv'
```

#### Exemplo de Resposta:

```json
{
  "message": "Arquivos processados com sucesso!",
  "data": {
    "media_geral": 75.6,
    "alunos": [{ "nome": "Agamedes Redondo", "acertos": 22, "media": 73.3 },...]
  }
}
```

---

### 📊 2. Obter Resultados Processados

**Rota:** `/results/`
**Método:** `GET`

#### Exemplo de Requisição `cURL`

```sh
curl -X 'GET' 'http://127.0.0.1:8000/results/' -H 'accept: application/json'
```

#### Exemplo de Resposta:

```json
{
  "media_geral": 75.6,
  "alunos": [{ "nome": "Agamedes Redondo", "acertos": 22, "media": 73.3 }]
}
```

---

## 📝 Considerações

- Caso os arquivos CSV não estejam no formato correto, a API retornará um erro.
- É necessário fazer upload dos arquivos antes de consultar os resultados.
- Para testes, utilize os arquivos `gabarito.csv` e `respostas.csv` fornecidos no enunciado.

---

## 🛠️ Melhorias Futuras

- Exportação dos resultados para CSV ou PDF.
- Interface web para upload e visualização dos resultados.
- Integração com um banco de dados para armazenar histórico de resultados.

---

## 📜 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo. 😊
