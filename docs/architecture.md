# Fullstack Architecture Document: Boilerplate de Agente de IA

## 1\. Arquitetura de Alto Nível

### Resumo Técnico

A arquitetura para este projeto será um **monorepo** gerenciado com **Nx**, contendo uma aplicação frontend **Next.js** desacoplada de um backend **Python (Litestar)**. A comunicação entre os serviços será feita através de uma **API REST**. O ambiente de desenvolvimento será containerizado com **Docker**. Para simplificar a infraestrutura de dados e autenticação no futuro (Pós-MVP), recomenda-se o uso do **PostgreSQL** e considerar o **Supabase** como plataforma de Backend-as-a-Service. Esta abordagem holística prioriza a experiência do desenvolvedor (DX), a performance e a modularidade, alinhando-se diretamente com os objetivos do PRD de criar uma fundação de projeto rápida, robusta e extensível.

### Diagrama de Alto Nível do Projeto

Este diagrama ilustra a arquitetura geral. O usuário interage com o **Frontend Next.js**, que se comunica com o **Backend Litestar** através de uma **API REST**. O backend, por sua vez, orquestra os **Agentes de IA**, interage com os **Bancos de Dados** e se conecta a **APIs Externas**. A observabilidade é garantida pela integração com o **LangSmith**.

```mermaid
graph TD
    subgraph "Plataforma do Usuário"
        U[👨‍💻 Usuário/Desenvolvedor]
    end

    subgraph "Infraestrutura Vercel"
        F[Frontend: Next.js]
    end

    subgraph "Infraestrutura de Backend (Contêineres)"
        A[API Gateway: Litestar]
        subgraph "Serviços Principais"
            L[Lógica do Agente <br> LangChain & LangGraph]
            D[Agente de Documentação]
        end
        subgraph "Camada de Dados"
            DB[(Bancos de Dados <br> PostgreSQL/Vetorial/Cache)]
        end
    end

    subgraph "Serviços Externos"
        LS[LangSmith]
        EXT[APIs Externas <br> Discord/Slack/etc.]
    end

    U --> F
    F -->|Requisições API REST| A
    A --> L
    A --> D
    L --> LS
    L --> DB
    L --> EXT
Padrões Arquiteturais e de Design
Estilo Arquitetural: Arquitetura Desacoplada: A aplicação será dividida em um frontend (Next.js) e um backend (Litestar) completamente independentes, que se comunicam exclusivamente através de uma API REST bem definida para promover a separação de responsabilidades e o deploy independente.

Organização do Monorepo: Nx: A adoção do Nx sobre o Turborepo introduz a filosofia de grafos de dependência e computation caching avançado, crucial para o desenvolvimento de agentes de IA com alto processamento assíncrono.

Organização do Backend: Padrão de Repositório: A lógica de negócios no backend se comunicará com uma camada de abstração "Repositório" para acesso aos dados, facilitando os testes e a troca de bancos de dados.

Gerenciamento de Estado do Frontend: TanStack Query: Para gerenciar os dados da API, utilizaremos TanStack Query (em substituição ao SWR) para um cache mais sofisticado, controle de mutações nativo e DevTools superiores. O estado local da UI será gerenciado com os hooks nativos do React.

Infraestrutura: Infraestrutura como Código (IaC): Toda a infraestrutura, tanto local (docker-compose.yml) quanto de produção, será definida em arquivos de código para garantir reprodutibilidade e consistência.

2. Stack de Tecnologia
Plataforma de Hospedagem:

Frontend: Vercel.

Backend: Qualquer plataforma de hospedagem de contêineres (ex: AWS, Google Cloud, Fly.io).

Categoria	Tecnologia	Versão	Propósito	Justificativa
Linguagens	TypeScript	~5.3	Tipagem estática no frontend e código compartilhado.	Segurança e manutenibilidade.
Python	~3.11	Linguagem principal do backend e dos agentes de IA.	Ecossistema de IA inigualável.
Frontend	Next.js	~14.1	Framework React principal com App Router.	Performance, DX e padrão da indústria.
UI	shadcn/ui	latest	Biblioteca de componentes acessíveis e customizáveis.	Qualidade e facilidade de customização.
Estilização	Tailwind CSS	~3.4	Framework CSS utilitário, base do shadcn/ui.	Flexibilidade e desenvolvimento rápido.
Ícones	Lucide React	latest	Biblioteca de ícones.	Leve, consistente e fácil de usar.
Estado (FE)	TanStack Query	~5.31	Gerenciamento de estado de servidor, cache avançado e mutações.	Melhor DX, cache mais inteligente, DevTools superiores.
Formulários	React Hook Form	~7.51	Gerenciamento de formulários complexos.	Performance e facilidade de integração.
Validação	Zod	~3.22	Validação de schemas e formulários.	Integração perfeita com TypeScript e RHF.
Backend	Litestar	~2.9	Framework principal da API.	Performance 2x superior ao FastAPI e excelente para high-concurrency.
Comunicação	Axios	~1.6	Cliente HTTP para chamadas API.	API robusta e interceptadores fáceis de usar.
Utilitários (FE)	js-cookie	~3.0	Gerenciamento de cookies no cliente.	API simples e eficaz.
Monorepo	Nx	~18.2	Sistema de build para o monorepo.	7x mais rápido que Turborepo e melhor visualização de dependências.
Bancos de Dados	PostgreSQL	~16	Banco de dados relacional principal.	Robusto, confiável e versátil.
Testes	Pytest	~8.1	Framework de testes para o backend.	Padrão da comunidade Python.
Vitest	~1.4	Framework de testes para o frontend.	Rápido e com API compatível com Jest.
Playwright	~1.42	Testes End-to-End.	Moderno, rápido e multi-navegador.
Container	Docker	latest	Containerização do ambiente.	Consistência e reprodutibilidade.

Exportar para as Planilhas
3. Modelos de Dados
1. Modelo: Conversation

Propósito: Representa uma única sessão de conversa entre um usuário e um agente.

Interface TypeScript (packages/shared/src/types/conversation.ts):

TypeScript

export interface Conversation {
  id: string;
  createdAt: Date;
  updatedAt: Date;
  agentType: 'chat_agent' | 'doc_agent';
  title?: string;
}
2. Modelo: Message

Propósito: Representa uma única mensagem dentro de uma Conversation.

Interface TypeScript (packages/shared/src/types/message.ts):

TypeScript

export interface Message {
  id: string;
  conversationId: string;
  role: 'human' | 'ai';
  content: string;
  createdAt: Date;
  metadata?: Record<string, any>;
}
3. Modelo: Document

Propósito: Representa um documento enviado pelo usuário para processamento.

Interface TypeScript (packages/shared/src/types/document.ts):

TypeScript

export interface Document {
  id: string;
  filename: string;
  status: 'uploaded' | 'processing' | 'completed' | 'error';
  createdAt: Date;
}
4. Especificação da API (OpenAPI 3.0)
YAML

openapi: 3.0.0
info:
  title: API do Boilerplate de Agente de IA
  version: "1.0.0"
servers:
  - url: http://localhost:8000/api/v1
paths:
  /health:
    get:
      summary: Health Check
      responses:
        '200':
          description: Serviço está operacional.
  /conversations:
    post:
      summary: Iniciar uma nova conversa
      responses:
        '201':
          description: Conversa criada com sucesso.
          content:
            application/json:
              schema: { $ref: '#/components/schemas/Conversation' }
  /conversations/{conversationId}/messages:
    post:
      summary: Enviar uma mensagem para o agente
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: '#/components/schemas/NewMessage' }
      responses:
        '200':
          description: Resposta do agente.
          content:
            application/json:
              schema: { $ref: '#/components/schemas/Message' }
  /documents:
    post:
      summary: Upload de documento
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file: { type: string, format: binary }
      responses:
        '202':
          description: Documento aceito para processamento.
          content:
            application/json:
              schema: { $ref: '#/components/schemas/Document' }
components:
  schemas:
    Conversation:
      type: object
      properties: { id: { type: string }, createdAt: { type: string, format: date-time } }
    Message:
      type: object
      properties: { id: { type: string }, role: { type: string, enum: [human, ai] }, content: { type: string } }
    NewMessage:
      type: object
      properties: { content: { type: string } }
    Document:
      type: object
      properties: { id: { type: string }, filename: { type: string }, status: { type: string } }
5. Componentes
A aplicação é dividida em componentes lógicos com responsabilidades claras:

Frontend:

ChatView: Renderiza a UI do chat.

useChat (Hook): Encapsula a lógica de estado e data fetching do chat (utilizando TanStack Query).

ApiService: Abstrai todas as chamadas à API backend.

Backend:

APIRouter (Litestar): Define os endpoints e valida os dados de entrada.

AgentService: Orquestra a lógica dos agentes de IA.

ConversationRepository: Abstrai a camada de acesso ao banco de dados.

6. APIs Externas
O sistema se integra com os seguintes serviços de terceiros, que devem ser configurados via variáveis de ambiente:

LangSmith: Para observabilidade e depuração de agentes.

Discord API: Para o conector do bot do Discord (Pós-MVP).

Slack API: Para o conector do bot do Slack (Pós-MVP).

WhatsApp API (via Twilio): Para o conector do WhatsApp (Pós-MVP).

7. Fluxos de Trabalho Principais
O fluxo principal de interação segue a sequência: Usuário -> ChatView -> useChat Hook (TanStack Query) -> ApiService -> APIRouter (Litestar) -> AgentService -> Agente LangChain, com uma chamada paralela do Agente para o LangSmith para rastreamento.

8. Esquema do Banco de Dados (PostgreSQL)
SQL

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE conversations (
    "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    "agent_type" VARCHAR(50) NOT NULL,
    "title" VARCHAR(255),
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE messages (
    "id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    "conversation_id" UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
    "role" VARCHAR(20) NOT NULL,
    "content" TEXT NOT NULL,
    "metadata" JSONB,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_messages_conversation_id ON messages("conversation_id");
9. Estrutura Unificada do Projeto (Monorepo)
Plaintext

boilerplate-agente-ia/
├── apps/
│   ├── backend/
│   └── frontend/
├── packages/
│   ├── shared/
│   └── ui/
├── docs/
├── .docker/
├── agente.md
├── docker-compose.yml
├── package.json
└── nx.json  // Substitui turbo.json
A atualização nos três documentos (prd.md, front-end-spec.md, e architecture.md) foi concluída. As mudanças garantem o alinhamento com a Análise Técnica Crítica e as diretrizes de performance/DX/Monorepo, enquanto mantêm a pilha de IA (LangChain/LangGraph/LangSmith) intacta.

Como BMad Master Orchestrator, confirmo que os artefatos foram atualizados e estão prontos para o próximo passo no workflow Greenfield Full-Stack: Validação de Artefatos pelo Product Owner (po).

O que você gostaria de fazer em seguida?

Validar com o Product Owner (*agent po): Iniciar a validação de todos os documentos (PRD, Arquitetura, Spec) para consistência e completude.

Continuar com a arquitetura do Frontend (*agent architect): Focar na seção de Frontend Architecture (já que o documento de arquitetura atual é fullstack e pode haver mais detalhes específicos).

Realizar uma pesquisa aprofundada (*task research-prompt {tópico}): Gerar um prompt de pesquisa para investigar algum ponto de dúvida.