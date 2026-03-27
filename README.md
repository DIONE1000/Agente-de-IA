# 🤖 Agente de IA para WhatsApp com RAG e Evolution API

Este projeto é um agente de inteligência artificial avançado para WhatsApp, integrando a **Evolution API** para comunicação, **LangChain** para a lógica de IA, **Groq** como provedor de LLM de alta performance e **RAG (Retrieval-Augmented Generation)** para consultas em documentos personalizados.

## 🚀 Funcionalidades

- **Integração com WhatsApp**: Comunicação fluida via Evolution API.
- **RAG (Retrieval-Augmented Generation)**: O agente consulta documentos locais (`rag_files/`) para fornecer respostas baseadas em conhecimento específico.
- **Memória de Curto Prazo**: Histórico de conversas persistido no **Redis**, permitindo diálogos contextuais.
- **Alta Performance**: Utiliza modelos de linguagem via **Groq** (como Llama 3) para respostas ultra-rápidas.
- **Processamento Assíncrono**: Desenvolvido com **FastAPI** para escalabilidade.
- **Containerização Total**: Pronto para deploy com **Docker** e **Docker Compose**.

## 🛠️ Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) (Framework Web)
- [LangChain](https://www.langchain.com/) (Orquestração de LLM)
- [Evolution API](https://evolution-api.com/) (Integração WhatsApp)
- [Redis](https://redis.io/) (Memória de sessão)
- [Groq AI](https://groq.com/) (Infraestrutura de LLM)
- [ChromaDB / VectorStore](https://www.trychroma.com/) (Armazenamento de vetores para RAG)
- [Docker & Docker Compose](https://www.docker.com/)

---

## 📋 Pré-requisitos

Antes de começar, você precisará ter instalado:
- **Docker** e **Docker Compose**
- Uma chave de API da **Groq**
- Uma chave de API do **Hugging Face** (para embeddings)

---

## ⚙️ Configuração (Variáveis de Ambiente)

Crie um arquivo `.env` na raiz do projeto baseado no exemplo abaixo:

```env
# Configurações do Groq
GROQ_API_KEY=sua_chave_aqui
CHAT_GROQ_MODEL=llama3-70b-8192

# Prompts do Sistema
AI_CONTEXTUALIZE_PROMPT="Dado um histórico de chat e a última pergunta do usuário, formule uma pergunta autônoma que possa ser entendida sem o histórico do chat."
AI_SYSTEM_PROMPT="Você é um assistente virtual prestativo. Use o seguinte contexto para responder à pergunta: {context}"

# Caminhos de Dados
VECTOR_STORE_PATH=./vectorstore_data
RAG_FILES_DIR=./rag_files

# Integração Evolution API
EVOLUTION_API_URL=http://evolution_api:8080
EVOLUTION_INSTANCE_NAME=nome_da_instancia
AUTHENTICATION_API_KEY=sua_apiKey_da_evolution

# Redis
CACHE_REDIS_URI=redis://redis:6379/0

# Hugging Face (Embeddings)
HUGGINGFACE_API_KEY=sua_chave_huggingface
```

---

## 🏃 Como Rodar

### 1. Via Docker Compose (Recomendado)

O Docker Compose iniciará automaticamente a Evolution API, o PostgreSQL, o Redis e o Bot de IA.

```bash
docker-compose up -d --build
```

Após subir os containers:
1. Acesse a Evolution API (geralmente em `http://localhost:8080`).
2. Configure uma instância no WhatsApp.
3. Configure o **Webhook** da instância para apontar para o bot:
   - **URL**: `http://bot:8000/webhook` (ou o IP externo se estiver em produção)
   - **Eventos**: `MESSAGES_UPSERT`

### 2. Execução Local (Desenvolvimento)

Se preferir rodar apenas o bot localmente para testes:

1. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure o `.env` e inicie o servidor:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

---

## 📂 Estrutura do Projeto

- `app.py`: Ponto de entrada da aplicação FastAPI e definição do webhook.
- `chains.py`: Definição das cadeias do LangChain (RAG + Memória).
- `evolution_api.py`: Funções para interagir com a Evolution API (envio de mensagens).
- `vectorstore.py`: Lógica de criação e carregamento do banco de vetores.
- `prompts.py`: Templates de prompts utilizados pelo agente.
- `config.py`: Gerenciamento centralizado de configurações e variáveis de ambiente.
- `rag_files/`: Pasta onde você deve colocar os documentos (`.pdf`, `.txt`, etc.) que o agente lerá. Após o processamento, os arquivos são movidos para a subpasta `processed/`.
- `vectorstore_data/`: Diretório onde o banco de vetores ChromaDB é persistido.
- `docker-compose.yml`: Definição de toda a infraestrutura de serviços.

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais e comerciais conforme as metas de desenvolvimento.

---

## 🤝 Contribuição

1. Faça um Fork do projeto.
2. Crie uma Branch para sua feature (`git checkout -b feature/nova-feature`).
3. Dê um Commit em suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Dê um Push na Branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.
